"""Package for tests of the entry point."""
from click.testing import CliRunner

from stack.cli import cli


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert ' tvm ' in result.output
