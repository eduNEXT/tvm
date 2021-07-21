"""Entry point for all the `stack *` commands."""

import click

from stack import __version__
from stack.config import config_command
from stack.strain import strain_command
from stack.tvm import tvm_command


def main() -> None:
    """Hold all the commands in a group."""
    cli()


@click.group(context_settings={"help_option_names": ["-h", "--help", "help"]})
@click.version_option(version=__version__)
def cli() -> None:
    """Define the main `stack` group."""


if __name__ == "__main__":
    main()

cli.add_command(tvm_command)
cli.add_command(config_command)
cli.add_command(strain_command)
