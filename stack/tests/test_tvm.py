"""Package for tests of the tutor version manager."""
import pytest
from click.exceptions import BadParameter
from click.testing import CliRunner

from stack.tvm import tvm_command, validate_version


def test_tvm_help():
    runner = CliRunner()
    result = runner.invoke(tvm_command)

    assert result.exit_code == 0
    assert ' install ' in result.output
    assert ' uninstall ' in result.output
    assert ' list ' in result.output
    assert ' setup ' in result.output
    assert ' use ' in result.output


def test_version_validator():
    with pytest.raises(BadParameter):
        validate_version(None, None, 'v12.0.')
