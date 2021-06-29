"""Package for tests of the tutor version manager."""
from click.testing import CliRunner

from stack.config import config_command


def test_tvm_help():
    runner = CliRunner()
    result = runner.invoke(config_command)

    assert result.exit_code == 0
    assert ' use ' in result.output
