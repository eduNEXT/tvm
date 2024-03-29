"""Package for tests of the tutor version manager."""
import pytest
from click.exceptions import BadParameter
from click.testing import CliRunner

from tvm.cli import cli, install, validate_version, projects


def test_should_return_all_tvm_cli_commands():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert ' install ' in result.output
    assert ' uninstall ' in result.output
    assert ' list ' in result.output
    assert ' use ' in result.output
    assert ' plugins ' in result.output


def test_should_fail_if_format_version_is_not_valid():
    with pytest.raises(BadParameter):
        validate_version(None, None, 'v12.0.')


def test_should_fail_if_version_does_not_exist():
    runner = CliRunner()
    result = runner.invoke(install, ["v0.0.99"])
    assert 'Could not find target: v0.0.99' in result.stdout


def test_should_return_all_tvm_project_commands():
    runner = CliRunner()
    result = runner.invoke(projects)

    assert result.exit_code == 0
    assert ' init ' in result.output
