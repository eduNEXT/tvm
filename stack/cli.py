"""Entry point for all the `stack *` commands."""

import click

from stack import __version__
from stack.tvm import tvm_command


def main() -> None:
    """Hold all the commands in a group."""
    cli.add_command(tvm_command)
    cli()


@click.group(context_settings={"help_option_names": ["-h", "--help", "help"]})
@click.version_option(version=__version__)
def cli() -> None:
    """Define the main `stack` group."""


if __name__ == "__main__":
    main()
