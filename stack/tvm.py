'''
Tutor version manager, inspired in nvm for node
'''
import os
import sys

import click
import requests


VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"


@click.group(name="tvm", short_help="Tutor Version Manager")
def tvm_command() -> None:
    pass


def setup_tvm():
    """
    """
    os.mkdir(path)
    # os.path.join(parent_dir, directory


@click.command(name="list")
@click.option('-l', '--limit', default=50, help='number of `latest versions` to list')
def list_versions(limit: int):
    """
    Get all the versions from github and
    mark the installed ones and the current.
    """
    api_info = requests.get(f'{VERSIONS_URL}?per_page={limit}').json()

    click.echo(f'Listing the latest {limit} versions of tutor')

    version_names = [x.get('name') for x in api_info]
    for name in version_names:
        click.echo(click.style(name, fg='yellow'))


@click.command(name="install")
@click.argument('version')
def install(version: str):
    """
    Install the given VERSION of tutor in the .tvm directory
    """
    click.echo(f'Will install {version}')


@click.command(name="uninstall")
@click.argument('version')
def uninstall(version: str):
    """
    Install the given VERSION of tutor in the .tvm directory
    """
    click.echo(f'Will install {version}')


@click.command(name="use")
@click.argument('version')
def use(version: str):
    """
    Configures the path to use VERSION
    """
    click.echo(f'Will use {version}')


tvm_command.add_command(list_versions)
tvm_command.add_command(install)
tvm_command.add_command(uninstall)
