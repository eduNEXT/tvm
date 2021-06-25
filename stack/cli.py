import sys

import click

from stack import __version__
from stack.tvm import tvm_command


# stack juniper start -> local
# stack tvm start -> local
# stack juniper start -> local


# instalar tutor versions
# manejar tutor version




def main() -> None:
    cli.add_command(tvm_command)

    cli.add_command(dropdb)

    cli()  # pylint: disable=no-value-for-parameter


@click.group(context_settings={"help_option_names": ["-h", "--help", "help"]})
@click.version_option(version=__version__)
def cli() -> None:
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')



if __name__ == "__main__":
    main()

# /data/eduNEXT/ws-producto/tools/stack-builder/tutor_envs/tutor_12_src/venv12/bin/tutor --version

