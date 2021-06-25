"""Package for tests of the tutor version manager."""
from click.testing import CliRunner

from stack.tvm import tvm_command


def test_tvm_help():
    runner = CliRunner()
    result = runner.invoke(tvm_command)

    assert result.exit_code == 0
    assert ' install ' in result.output
    assert ' uninstall ' in result.output
    assert ' list ' in result.output
    assert ' setup ' in result.output
    assert ' use ' in result.output
