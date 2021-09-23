"""Tutor version manager, inspired in nvm for node."""
import datetime
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import zipfile
from distutils.version import LooseVersion

import click
import requests
from jinja2 import Template

VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
TVM_PATH = pathlib.Path().resolve() / '.tvm'


@click.group(name="tvm", short_help="Tutor Version Manager")
def tvm_command() -> None:
    """Hold the main wrapper for the `stack tvm` command."""


def validate_version(ctx, param, value):  # pylint: disable=unused-argument
    """Raise BadParameter if the value is not a tutor version."""
    result = re.match(r'^v([0-9]+)\.([0-9]+)\.([0-9]+)$', value)
    if not result:
        raise click.BadParameter("format must be 'vX.Y.Z'")

    return value


def get_local_versions():
    """Return a list of strings with the local version installed. If None, returns empty array."""
    if os.path.exists(f'{TVM_PATH}'):
        return [x for x in os.listdir(f'{TVM_PATH}') if os.path.isdir(f'{TVM_PATH}/{x}')]
    return []


def validate_version_installed(ctx, param, value):  # pylint: disable=unused-argument
    """Raise BadParameter if the value is not a tutor version."""
    validate_version(ctx, param, value)

    local_versions = get_local_versions()
    if value not in local_versions:
        raise click.BadParameter("You must install the version before using it.\n\n"
                                 "Use `stack tvm list` for available versions.")

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
            "active": None,
            "tutor_root": None,
        }
        with open(info_file_path, 'w', encoding='utf-8') as info_file:
            json.dump(data, info_file, indent=4)


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

    active = get_active_version()

    for name in version_names:
        color = 'yellow'
        if name in local_versions:
            color = 'green'
        if name == active:
            name = f'{name} <-- active'
        click.echo(click.style(name, fg=color))


@click.command(name="install")
@click.option('-f', '--force', is_flag=True, help='Uninstall before running')
@click.argument('version', callback=validate_version)
def install(force: bool, version: str):
    """Install the given VERSION of tutor in the .tvm directory."""
    setup_tvm()

    if force:
        do_uninstall(version=version)

    try:
        os.mkdir(f'{TVM_PATH}/{version}')
    except FileExistsError as error:
        raise click.UsageError(click.style(f'Already exists a directory {version}. Uninstall first.',
                                           fg='red')) from error

    # Find the target version info
    api_info = requests.get(f'{VERSIONS_URL}?per_page=100').json()
    try:
        target = [x for x in api_info if x.get('name') == version][0]
        # print target data to dir
        target['installation_date'] = str(datetime.datetime.now())
        with open(f'{TVM_PATH}/{version}/info.json', 'w', encoding='utf-8') as info_file:
            json.dump(target, info_file, indent=4)
    except IndexError as error:
        raise click.UsageError(f'Could not find target: {version}') from error

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

    # Create virtualenv
    subprocess.run(f'cd {TVM_PATH}/{version}; virtualenv venv',
                   shell=True, check=True,
                   executable='/bin/bash')

    # Install tutor
    subprocess.run(f'source {TVM_PATH}/{version}/venv/bin/activate;'
                   f'pip install -e {TVM_PATH}/{version}/overhangio-tutor-*/',
                   shell=True, check=True,
                   executable='/bin/bash')


def do_uninstall(version: str):
    """Uninstall the version by deleting the dir."""
    try:
        shutil.rmtree(f'{TVM_PATH}/{version}')
    except FileNotFoundError:
        click.echo('Nothing to uninstall for this version')


@click.command(name="uninstall")
@click.argument('version')
def uninstall(version: str):
    """Install the given VERSION of tutor in the .tvm directory."""
    do_uninstall(version=version)


def get_active_version() -> str:
    """Read the current active version from the json/bash switcher."""
    info_file_path = f'{TVM_PATH}/current_bin.json'
    if os.path.exists(info_file_path):
        with open(info_file_path, 'r', encoding='utf-8') as info_file:
            data = json.load(info_file)
        return data.get('active', 'Invalid active version')
    return 'No active version installed'


def set_active_version(version) -> None:
    """Set the active version in the json to VERSION."""
    info_file_path = f'{TVM_PATH}/current_bin.json'

    with open(info_file_path, 'r', encoding='utf-8') as info_file:
        data = json.load(info_file)

    data['active'] = version

    with open(info_file_path, 'w', encoding='utf-8') as info_file:
        json.dump(data, info_file, indent=4)


def set_switch_from_file() -> None:
    """Set the active version from the json into the switcher."""
    info_file_path = f'{TVM_PATH}/current_bin.json'

    with open(info_file_path, 'r', encoding='utf-8') as info_file:
        data = json.load(info_file)

    with open('stack/templates/tutor_switcher.j2', encoding='utf-8') as template:
        switcher = Template(template.read())

    try:
        config_name = '/'.join(data['tutor_root'].split('/')[-3:])
    except:  # pylint: disable=bare-except
        config_name = data.get('tutor_root', None)

    context = {
        'version': data.get('active', None),
        'tutor_root': data.get('tutor_root', None),
        'config_name': config_name,
        'tvm': TVM_PATH,
    }

    switcher_file = f'{TVM_PATH}/tutor_switcher'
    with open(switcher_file, mode='w', encoding='utf-8') as of_text:
        of_text.write(switcher.render(**context))

    # set execute permissions
    os.chmod(switcher_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)


def install_venv() -> None:
    """Make the switcher file available to the virtualenv path."""
    # link from the venv
    venv_tutor = pathlib.Path(sys.executable).parent.joinpath('tutor').resolve()
    try:
        os.symlink(f'{TVM_PATH}/tutor_switcher', venv_tutor)
    except FileExistsError:
        pass
    else:
        click.echo(click.style(
            'Re-activate your virtualenv for changes to take effect', fg='yellow'))


@click.command(name="setup")
@click.option('-g', '--global', 'make_global', is_flag=True, help='Make the tutor command available to the cli')
def install_global(make_global) -> None:
    """Make the switcher file to anyone in the system."""
    setup_tvm()
    set_switch_from_file()
    install_venv()

    if make_global:
        try:
            os.symlink(f'{TVM_PATH}/tutor_switcher', '/usr/local/bin/tutor')
        except PermissionError:
            subprocess.call(['sudo', 'ln', '-s', f'{TVM_PATH}/tutor_switcher', '/usr/local/bin/tutor'])
        except FileExistsError:
            click.echo('There is already a file at: /usr/local/bin/tutor')


@click.command(name="use")
@click.argument('version', callback=validate_version_installed)
def use(version: str):
    """Configure the path to use VERSION."""
    setup_tvm()
    set_active_version(version)
    set_switch_from_file()


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


@click.command(name="pip", context_settings={"ignore_unknown_options": True})
@click.argument('options', nargs=-1, type=click.UNPROCESSED)
def pip(options):
    """Use the package installer pip in current tutor version."""
    click.echo(run_on_tutor_venv('pip', options))


@click.group(name="plugins")
def plugins() -> None:
    """Use plugins commands."""


@click.command(name="list")
def list_plugins():
    """List installed plugins by tutor version."""
    active = get_active_version()
    local_versions = get_local_versions()
    for version in local_versions:
        version = str(version)
        if version == active:
            click.echo(click.style(f"{version} < -- active", fg='green'))
        else:
            click.echo(click.style(version, fg='green'))

        click.echo(run_on_tutor_venv('tutor', ['plugins', 'list'], version=version))

    click.echo('Note: the disabled notice depends on the active strain configuration.')


tvm_command.add_command(list_versions)
tvm_command.add_command(install)
tvm_command.add_command(uninstall)
tvm_command.add_command(use)
tvm_command.add_command(install_global)
tvm_command.add_command(pip)
tvm_command.add_command(plugins)
plugins.add_command(list_plugins)
