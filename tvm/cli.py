"""Entry point for all the `tvm *` commands."""
import datetime
import json
import os
import pathlib
import random
import re
import shutil
import stat
import string
import subprocess
import sys
import zipfile
from distutils.dir_util import copy_tree
from distutils.version import LooseVersion
from typing import Optional

import click
import requests
from click.shell_completion import CompletionItem

from tvm import __version__
from tvm.templates.tutor_switcher import TUTOR_SWITCHER_TEMPLATE
from tvm.templates.tvm_activate import TVM_ACTIVATE_SCRIPT

VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
TVM_PATH = pathlib.Path.home() / '.tvm'


def main() -> None:
    """Hold all the commands in a group."""
    cli()


@click.group(
    name="tvm",
    short_help="Tutor Version Manager",
    context_settings={"help_option_names": ["--help", "-h", "help"]}
)
@click.version_option(version=__version__)
def cli() -> None:
    """Define the main `tvm` group."""


class TutorVersionType(click.ParamType):
    """Provide autocomplete functionability for tutor versions."""

    def shell_complete(self, ctx, param, incomplete):
        """Provide autocomplete for shell."""
        return [
            CompletionItem(name)
            for name in get_local_versions() if name.startswith(incomplete)
        ]


def version_is_valid(value):
    """Raise BadParameter if the value is not a tutor version."""
    result = re.match(r'^v([0-9]+)\.([0-9]+)\.([0-9]+)$', value)
    if not result:
        raise click.BadParameter("format must be 'vX.Y.Z'")

    return value


def validate_version(ctx, param, value):  # pylint: disable=unused-argument
    """Raise BadParameter if the value is not a tutor version."""
    return version_is_valid(value)


def get_local_versions():
    """Return a list of strings with the local version installed. If None, returns empty array."""
    if os.path.exists(f'{TVM_PATH}'):
        return [x for x in os.listdir(f'{TVM_PATH}') if os.path.isdir(f'{TVM_PATH}/{x}')]
    return []


def version_is_installed(value) -> bool:
    """Return false if the value is not installed."""
    version_is_valid(value)
    local_versions = get_local_versions()
    return value in local_versions


def validate_version_installed(ctx, param, value):  # pylint: disable=unused-argument
    """Raise BadParameter if the value is not a tutor version."""
    is_installed = version_is_installed(value)
    if not is_installed:
        raise click.BadParameter("You must install the version before using it.\n\n"
                                 "Use `tvm list` for available versions.")
    return value


def setup_tvm():
    """
    Initialize the directory for all tutor versions.

    Can be called at any time, since it should not damage anything.
    """
    try:
        os.mkdir(TVM_PATH)
    except FileExistsError:
        pass

    info_file_path = f'{TVM_PATH}/current_bin.json'
    if not os.path.exists(info_file_path):
        data = {
            "version": None,
            "tutor_root": None,
            "tutor_plugins_root": None,
        }
        with open(info_file_path, 'w', encoding='utf-8') as info_file:
            json.dump(data, info_file, indent=4)

    set_switch_from_file(file=info_file_path)

    tutor_switcher = f'{TVM_PATH}/tutor_switcher'
    try:
        os.symlink(tutor_switcher, '/usr/local/bin/tutor')
    except PermissionError:
        subprocess.call(['sudo', 'ln', '-s', tutor_switcher, '/usr/local/bin/tutor'])
    except FileExistsError:
        pass


def setup_version_virtualenv(version=None) -> None:
    """Create virtualenv and install tutor cloned."""
    # Create virtualenv
    subprocess.run(f'cd {TVM_PATH}/{version}; virtualenv venv',
                   shell=True, check=True,
                   executable='/bin/bash')

    # Install tutor
    subprocess.run(f'source {TVM_PATH}/{version}/venv/bin/activate;'
                   f'pip install -e {TVM_PATH}/{version}/overhangio-tutor-*/',
                   shell=True, check=True,
                   executable='/bin/bash')


@click.command(name="list")
@click.option('-l', '--limit', default=10, help='number of `latest versions` to list')
def list_versions(limit: int):
    """
    Get all the versions from github.

    Print and mark the both the installed ones and the current.
    """
    # from github
    api_info = requests.get(f'{VERSIONS_URL}?per_page={limit}').json()
    api_versions = [x.get('name') for x in api_info]

    # from the local .tvm
    local_versions = get_local_versions()

    click.echo(f'Listing the latest {limit} versions of tutor')
    version_names = list(set(api_versions + local_versions))
    version_names = sorted(version_names, reverse=True, key=LooseVersion)

    project_version = None
    if "TVM_PROJECT_ENV" in os.environ:
        project_version = get_project_version(os.environ.get("TVM_PROJECT_ENV"))

    global_active = get_active_version()

    for name in version_names:
        color = 'yellow'
        if name in local_versions:
            color = 'green'
        if name == global_active:
            if project_version:
                color = 'blue'
                name = f'{name} (global)'
            else:
                name = f'{name} (active)'
        if project_version and project_version == name:
            name = f'{name} (active)'
        click.echo(click.style(name, fg=color))


@click.command(name="install")
@click.option('-f', '--force', is_flag=True, help='Uninstall before running')
@click.argument('version', callback=validate_version)
def install(force: bool, version: str):
    """Install the given VERSION of tutor in the .tvm directory."""
    setup_tvm()

    # Find the target version info
    api_info = requests.get(f'{VERSIONS_URL}?per_page=100').json()

    try:
        target = [x for x in api_info if x.get('name') == version][0]
    except IndexError:
        raise click.UsageError(f'Could not find target: {version}') from IndexError

    if force:
        do_uninstall(version=version)

    try:
        os.mkdir(f'{TVM_PATH}/{version}')
        target['installation_date'] = str(datetime.datetime.now())
        with open(f'{TVM_PATH}/{version}/info.json', 'w', encoding='utf-8') as info_file:
            json.dump(target, info_file, indent=4)
    except FileExistsError as error:
        raise click.UsageError(click.style(f'Already exists a directory {version}. Uninstall first.',
                                           fg='red')) from error

    # Get the code in zip format
    zipball_url = target.get('zipball_url')
    zipball_filename = f'{TVM_PATH}/{version}.zip'
    stream = requests.get(zipball_url, stream=True)
    with open(zipball_filename, 'wb') as target_file:
        for chunk in stream.iter_content(chunk_size=256):
            target_file.write(chunk)

    # Unzip it
    with zipfile.ZipFile(zipball_filename, "r") as ziped:
        ziped.extractall(f'{TVM_PATH}/{version}')

    # Delete artifact
    os.remove(zipball_filename)

    # Create virtualenv and install tutor
    setup_version_virtualenv(version)


def do_uninstall(version: str):
    """Uninstall the version by deleting the dir."""
    try:
        shutil.rmtree(f'{TVM_PATH}/{version}')
    except FileNotFoundError:
        click.echo('Nothing to uninstall for this version')


@click.command(name="uninstall")
@click.argument('version', type=TutorVersionType())
def uninstall(version: str):
    """Install the given VERSION of tutor in the .tvm directory."""
    do_uninstall(version=version)


def get_active_version() -> str:
    """Read the current active version from the json/bash switcher."""
    info_file_path = f'{TVM_PATH}/current_bin.json'
    if os.path.exists(info_file_path):
        with open(info_file_path, 'r', encoding='utf-8') as info_file:
            data = json.load(info_file)
        return data.get('version', 'Invalid active version')
    return 'No active version installed'


def get_project_version(tvm_project_path) -> str:
    """Read the current active version from the json/bash switcher."""
    info_file_path = f'{tvm_project_path}/config.json'
    with open(info_file_path, 'r', encoding='utf-8') as info_file:
        data = json.load(info_file)
    return data.get('version')


def get_current_info(file: str = None) -> Optional[dict]:
    """Get the JSON data from the config file."""
    if not file:
        if "TVM_PROJECT_ENV" in os.environ:
            project = os.environ.get("TVM_PROJECT_ENV")
            file = f"{project}/config.json"
        else:
            file = f'{TVM_PATH}/current_bin.json'

    data = None
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as info_file:
            data = json.load(info_file)
    return data


def put_current_info(data: dict, file: str = None) -> None:
    """Update JSON data in the config file."""
    if not file:
        if "TVM_PROJECT_ENV" in os.environ:
            project = os.environ.get("TVM_PROJECT_ENV")
            file = f"{project}/config.json"
        else:
            file = f'{TVM_PATH}/current_bin.json'

    if os.path.exists(file):
        with open(file, 'w', encoding='utf-8') as info_file:
            json.dump(data, info_file, indent=4)


def set_active_version(version) -> None:
    """Set the active version in the json to VERSION."""
    info_file_path = f'{TVM_PATH}/current_bin.json'

    data = get_current_info(file=info_file_path)
    data['version'] = version

    put_current_info(data=data, file=info_file_path)


def set_switch_from_file(file: str = None) -> None:
    """Set the active version from the json into the switcher."""
    data = get_current_info(file=file)

    context = {
        'version': data.get('version', None),
        'tutor_root': data.get('tutor_root', None),
        'tutor_plugins_root': data.get('tutor_plugins_root', None),
        'tvm': TVM_PATH,
    }

    switcher_file = f'{TVM_PATH}/tutor_switcher'
    with open(switcher_file, mode='w', encoding='utf-8') as of_text:
        of_text.write(TUTOR_SWITCHER_TEMPLATE.render(**context))

    # set execute permissions
    os.chmod(switcher_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)


@click.command(name="use")
@click.argument('version', callback=validate_version_installed, type=TutorVersionType())
def use(version: str):
    """Configure the path to use VERSION."""
    setup_tvm()
    set_active_version(version)
    file = f'{TVM_PATH}/current_bin.json'
    set_switch_from_file(file=file)


def get_env_by_tutor_version(version):
    """Get virtual environment by tutor version."""
    return f'{TVM_PATH}/{version}/venv'


def run_on_tutor_switcher(options, capture_output=True):
    """Run commands through the current tutor + config file."""
    options = " ".join(options)
    result = subprocess.run(f'{TVM_PATH}/tutor_switcher {options}',
                            shell=True, check=True,
                            executable='/bin/bash',
                            capture_output=capture_output)
    return result.stdout


def run_on_tutor_venv(cmd, options, version=None):
    """Run commands on the virtualenv where this tutor is installed."""
    if not version:
        version = get_active_version()
    target_venv = get_env_by_tutor_version(version)
    options = " ".join(options)
    try:
        result = subprocess.run(f'source {target_venv}/bin/activate &&'
                                f'{cmd} {options} && deactivate',
                                shell=True, check=True,
                                executable='/bin/bash',
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return result.stdout
    except subprocess.CalledProcessError as ex:
        click.echo(click.style(
            f'Error running venv commands: {ex.output}',
            fg='red',
        ))
        click.echo(ex)
        sys.exit(1)


@click.group(name="plugins")
def plugins() -> None:
    """Use plugins commands."""


@click.command(name="list")
def list_plugins():
    """List installed plugins by tutor version."""
    project_version = None
    if "TVM_PROJECT_ENV" in os.environ:
        project_version = get_project_version(os.environ.get("TVM_PROJECT_ENV"))

    global_active = get_active_version()

    local_versions = get_local_versions()
    for version in local_versions:
        version = str(version)

        if version == global_active:
            if project_version:
                click.echo(click.style(f"{version} (global)", fg='blue'))
            else:
                click.echo(click.style(f"{version} (active)", fg='green'))
        elif project_version and version == project_version:
            click.echo(click.style(f"{version} (active)", fg='green'))
        else:
            click.echo(click.style(version, fg='green'))

        click.echo(run_on_tutor_venv('tutor', ['plugins', 'list'], version=version))

    click.echo('Note: the disabled notice depends on the active tutor configuration.')


@click.group(
    name="project",
    short_help="Tutor Environment Manager",
    context_settings={"help_option_names": ["--help", "-h", "help"]}
)
@click.version_option(version=__version__)
def projects() -> None:
    """Hold the main wrapper for the `tvm project` command."""


def create_project(project: str) -> None:
    """Duplicate the version directory and rename it."""
    if not os.path.exists(f"{TVM_PATH}/{project}"):
        tutor_version = project.split("@")[0]
        tutor_version_folder = f"{TVM_PATH}/{tutor_version}"

        tvm_project = f"{TVM_PATH}/{project}"
        copy_tree(tutor_version_folder, tvm_project)

        shutil.rmtree(f"{tvm_project}/venv")
        setup_version_virtualenv(project)


@click.command(name="init")
@click.argument('name', required=False)
@click.argument('version', required=False)
def init(name: str = None, version: str = None):
    """Configure a new tvm project in the current path."""
    if not version:
        version = get_active_version()

    if not version_is_installed(version):
        raise click.UsageError(f'Could not find target: {version}')

    if not name:
        letters = string.ascii_letters
        name = ''.join(random.choice(letters) for i in range(10))

    version = f"{version}@{name}"

    tvm_project_folder = pathlib.Path().resolve()
    tvm_environment = tvm_project_folder / '.tvm'

    if not os.path.exists(tvm_environment):
        pathlib.Path(f"{tvm_environment}/bin").mkdir(parents=True, exist_ok=True)

        # Create config json
        tvm_project_config_file = f"{tvm_environment}/config.json"
        data = {
            "version": f"{version}",
            "tutor_root": f"{tvm_project_folder}",
            "tutor_plugins_root": f"{tvm_project_folder}/plugins"
        }
        with open(tvm_project_config_file, 'w', encoding='utf-8') as info_file:
            json.dump(data, info_file, indent=4)

        # Create activate script
        context = {
            "version": f"{version}",
            "tutor_root": f"{tvm_project_folder}",
            "tutor_plugins_root": f"{tvm_project_folder}/plugins"
        }
        activate_script = f"{tvm_environment}/bin/activate"
        with open(activate_script, 'w', encoding='utf-8') as activate_file:
            activate_file.write(TVM_ACTIVATE_SCRIPT.render(**context))

        # Create tutor switcher
        context = {
            'version': data.get('version', None),
            'tvm': f"{TVM_PATH}",
        }
        tutor_file = f"{tvm_environment}/bin/tutor"
        with open(tutor_file, 'w', encoding='utf-8') as switcher_file:
            switcher_file.write(TUTOR_SWITCHER_TEMPLATE.render(**context))
        # set execute permissions
        os.chmod(tutor_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

        create_project(project=version)
    else:
        raise click.UsageError('There is already a project initiated.') from IndexError


@click.command(name="install", context_settings={"ignore_unknown_options": True})
@click.argument('options', nargs=-1, type=click.UNPROCESSED)
def install_plugin(options):
    """Use the package installer pip in current tutor version."""
    options = list(options)
    options.insert(0, "install")
    if "TVM_PROJECT_ENV" in os.environ:
        run_on_tutor_venv('pip', options, version=get_project_version(os.environ.get("TVM_PROJECT_ENV")))
    else:
        run_on_tutor_venv('pip', options)


@click.group(
    name="config",
    short_help="TVM config variables",
    context_settings={"help_option_names": ["--help", "-h", "help"]}
)
@click.version_option(version=__version__)
def config() -> None:
    """Hold the main wrapper for the `tvm config` command."""


@click.command(name="save", context_settings={"ignore_unknown_options": True})
@click.option('--plugins-root', nargs=1, required=False, type=str)
@click.argument('root', required=True, type=str)
def save(root, plugins_root):
    """
    Set TUTOR_ROOT and TUTOR_PLUGINS_ROOT variables.

    You should write "." to set up the Current Working Directory as TUTOR_ROOT.

    TUTOR_PLUGINS_ROOT default is the TUTOR_ROOT/plugins.
    """
    if root == ".":
        root = os.getcwd()
    root = root.rstrip('/')

    if not plugins_root:
        plugins_root = f"{root}/plugins"
    plugins_root = plugins_root.rstrip('/')

    info_file_path = f'{TVM_PATH}/current_bin.json'
    data = get_current_info(file=info_file_path)
    data.update({
        "tutor_root": root,
        "tutor_plugins_root": plugins_root
    })
    put_current_info(data=data, file=info_file_path)
    set_switch_from_file(file=info_file_path)


@click.command(name="clear", context_settings={"ignore_unknown_options": True})
def clear():
    """Remove TUTOR_ROOT and TUTOR_PLUGINS_ROOT variables."""
    info_file_path = f'{TVM_PATH}/current_bin.json'
    data = get_current_info(file=info_file_path)
    data.update({
        "tutor_root": None,
        "tutor_plugins_root": None
    })
    put_current_info(data=data, file=info_file_path)
    set_switch_from_file(file=info_file_path)


if __name__ == "__main__":
    main()

cli.add_command(list_versions)
cli.add_command(install)
cli.add_command(uninstall)
cli.add_command(use)
cli.add_command(projects)
projects.add_command(init)
cli.add_command(plugins)
plugins.add_command(list_plugins)
plugins.add_command(install_plugin)
cli.add_command(config)
config.add_command(save)
config.add_command(clear)
