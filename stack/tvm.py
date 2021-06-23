'''
Tutor version manager, inspired in nvm for node
'''
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

import click
import requests

VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
TVM_PATH = '.tvm'


@click.group(name="tvm", short_help="Tutor Version Manager")
def tvm_command() -> None:
    pass


def validate_version(ctx, param, value):
    """
    Raise BadParameter if the value is not a tutor version.
    """
    result = re.match(r'^v([0-9]+)\.([0-9]+)\.([0-9]+)$', value)
    if not result:
        raise click.BadParameter("format must be 'vX.Y.Z'")

    return value


def setup_tvm():
    """
    Creates the directory for all tutor versions
    """
    try:
        os.mkdir(TVM_PATH)
    except FileExistsError:
        pass


@click.command(name="list")
@click.option('-l', '--limit', default=10, help='number of `latest versions` to list')
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
@click.option('-f', '--force', is_flag=True, help='Uninstall before running')
@click.argument('version', callback=validate_version)
def install(force: bool, version: str):
    """
    Install the given VERSION of tutor in the .tvm directory
    """
    setup_tvm()

    if force:
        do_uninstall(version=version)

    try:
        os.mkdir(f'{TVM_PATH}/{version}')
    except FileExistsError:
        raise click.UsageError(click.style(f'Already exists a directory {version}. Uninstall first.', fg='red'))

    # Find the target version info
    api_info = requests.get(f'{VERSIONS_URL}?per_page=100').json()
    try:
        target = [x for x in api_info if x.get('name') == version][0]
        # print target data to dir
        target['installation_date'] = str(datetime.datetime.now())
        with open(f'{TVM_PATH}/{version}/info.json', 'w') as info_file:
            json.dump(target, info_file, indent=4)
    except IndexError:
        raise click.UsageError(f'Could not find target: {version}')

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
    subprocess.run(f'source {TVM_PATH}/{version}/venv/bin/activate; pip install {TVM_PATH}/{version}/overhangio-tutor-*/',
        shell=True, check=True,
        executable='/bin/bash')


def do_uninstall(version: str):
    """
    Uninstalling is just deleting the dir.
    """
    try:
        shutil.rmtree(f'{TVM_PATH}/{version}')
    except FileNotFoundError:
        pass


@click.command(name="uninstall")
@click.argument('version')
def uninstall(version: str):
    """
    Install the given VERSION of tutor in the .tvm directory
    """
    do_uninstall(version=version)


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
