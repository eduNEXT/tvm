"""Manage the tutor_root and tutor environments."""
import json
import os
import pathlib

import click

from stack.tvm import TVM_PATH, set_switch_from_file, setup_tvm


@click.group(name="config", short_help="Manage tutor configurations and distribution strains")
def config_command() -> None:
    """Hold the main wrapper for the `stack config` command."""


def get_active_root() -> str:
    """Read the current active root config."""
    info_file_path = f'{TVM_PATH}/current_bin.json'

    if os.path.exists(info_file_path):
        with open(info_file_path, 'r', encoding='utf-8') as info_file:
            data = json.load(info_file)
        return data.get('tutor_root', 'Invalid config path')
    return 'No active config applied'


def set_active_root(path) -> None:
    """Set the active tutor_root in the json to PATH."""
    info_file_path = f'{TVM_PATH}/current_bin.json'

    with open(info_file_path, 'r', encoding='utf-8') as info_file:
        data = json.load(info_file)

    # clear tutor root
    if not path:
        data['tutor_root'] = None
    else:
        # check version for this tutor root configuration
        active_tutor = data.get('active')
        version_filepath = pathlib.Path(path).joinpath('env', 'version')
        if version_filepath.exists():
            with open(version_filepath, 'r', encoding='utf-8') as version_file:
                root_version = f'v{version_file.read()}'

            if root_version != active_tutor:
                click.echo(click.style(
                    'Incorrect version of tutor for this config.\n\n'
                    f'The tutor_root configuration you are loading uses {root_version}\n'
                    f'The active tutor version in TVM is {active_tutor}\n'
                    f'run: stack tvm use {root_version}',
                    fg='yellow'
                ))

        data['tutor_root'] = path

    with open(info_file_path, 'w', encoding='utf-8') as info_file:
        json.dump(data, info_file, indent=4)


def validate_root_path(ctx, param, value):  # pylint: disable=unused-argument
    """Raise BadParameter if the value is not a path to a tutor full configuration."""
    tutor_root = pathlib.Path(value)

    if not tutor_root.exists():
        raise click.BadParameter("The provided path does not exist.")

    if not tutor_root.joinpath('config.yml').exists():
        raise click.BadParameter("The provided path does not have a tutor configuration dir.")

    return str(tutor_root.resolve())


@click.command(name="use")
@click.argument('path', callback=validate_root_path)
def use(path: str):
    """Make tutor use the configuration file at PATH."""
    setup_tvm()
    set_active_root(path)
    set_switch_from_file()


@click.command(name="clear")
def clear():
    """Clear config files."""
    setup_tvm()
    set_active_root(path=None)
    set_switch_from_file()


config_command.add_command(use)
config_command.add_command(clear)
