"""Package for tests of the tutor version manager."""
from unittest import mock
from click.testing import CliRunner

import tvm.cli
from tvm.cli import cli, install, uninstall, projects, list_versions


def test_should_return_all_tvm_cli_commands():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    commands = ['config', 'install', 'uninstall', 'list', 'project', 'use', 'plugins']

    for command in commands:
        assert f' {command} ' in result.output


def test_should_fail_if_format_version_is_not_valid():
    runner = CliRunner()
    result = runner.invoke(install, ['v12.0.'])

    assert result.exit_code != 0


def test_should_fail_if_version_does_not_exist(requests_mock):
    # Given
    version = "v1.0.0"
    requests_mock.get(f'{tvm.cli.GET_TAG_URL}{version}', status_code=404)

    # When
    runner = CliRunner()
    result = runner.invoke(install, [version])

    # Then
    assert f'Could not find target: {version}' in result.stdout


def test_should_fail_if_version_is_not_installed():
    runner = CliRunner()
    result = runner.invoke(uninstall, ["v0.0.99"])
    assert 'Nothing to uninstall' in result.stdout


def test_should_return_all_tvm_project_commands():
    runner = CliRunner()
    result = runner.invoke(projects)

    assert result.exit_code == 0
    assert ' init ' in result.output


def test_should_list_all_tutor_versions_to_install(mocker, requests_mock):
    # Given
    test_versions = [{'name': 'test1'}, {'name': 'test2'}]
    requests_mock.get(f'{tvm.cli.VERSIONS_URL}?per_page=10', json=test_versions)
    mocker.patch('tvm.cli.get_local_versions', return_value=[])
    mocker.patch('tvm.cli.get_active_version', return_value=None)

    # When
    runner = CliRunner()
    result = runner.invoke(list_versions)

    # Then
    assert result.exit_code == 0
    for version in test_versions:
        assert version['name'] in result.output


def test_should_list_versions_and_mark_active_version(mocker, requests_mock):
    # Given
    test_versions = [{'name': 'v1.0.0'}, {'name': 'v2.0.0'}]
    test_global_version = test_versions[0]['name']
    requests_mock.get(f'{tvm.cli.VERSIONS_URL}?per_page=10', json=test_versions)

    current_bin_data_content = '{content}'.replace("content", f'"version": "{test_global_version}"')
    mocked_tvm_current_bin_data = mocker.mock_open(read_data=current_bin_data_content)
    mocker.patch("builtins.open", mocked_tvm_current_bin_data)

    mocker.patch('tvm.cli.get_local_versions', return_value=[])

    # When
    runner = CliRunner()
    result = runner.invoke(list_versions, ['-l', 10])

    # Then
    assert result.exit_code == 0
    assert f'{test_global_version} (active)' in result.output


@mock.patch.dict("os.environ", {"TVM_PROJECT_ENV": "/project/tvm"})
def test_should_list_versions_and_mark_active_project_version(mocker, requests_mock):
    # Given
    test_versions = [{'name': 'v1.0.0'}, {'name': 'v2.0.0'}]
    test_global_version = test_versions[0]['name']
    test_project_version = test_versions[1]['name']
    requests_mock.get(f'{tvm.cli.VERSIONS_URL}?per_page=10', json=test_versions)
    mocker.patch('tvm.cli.get_local_versions', return_value=[])
    mocker.patch('tvm.cli.get_active_version', return_value=test_global_version)

    project_config_data = '{content}'.replace("content", f'"version": "{test_project_version}"')
    mocked_project_tvm_config = mocker.mock_open(read_data=project_config_data)
    mocker.patch("builtins.open", mocked_project_tvm_config)

    # When
    runner = CliRunner()
    result = runner.invoke(list_versions, ['-l', 10])

    # Then
    assert result.exit_code == 0
    assert f'{test_project_version} (active)' in result.output
    assert f'{test_global_version} (global)' in result.output
