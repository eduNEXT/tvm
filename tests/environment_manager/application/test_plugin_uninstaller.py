import pytest

from tests.environment_manager.infrastructure.environment_manager_in_memory_repository import (
    EnvironmentManagerInMemoryRepository,
)
from tvm.environment_manager.application.plugin_uninstaller import (
    PluginUninstaller,
)


def test_should_uninstall_the_tutor_plugin():
    # Given
    options = "codejail"
    repository = EnvironmentManagerInMemoryRepository()

    # When
    uninstaller = PluginUninstaller(repository=repository)
    uninstaller(options)

    # Then
    assert options not in repository.PLUGINS_INSTALLED


def test_should_fail_if_not_add_tutor_plugin():
    # Given
    options = "tutor-mfe"
    repository = EnvironmentManagerInMemoryRepository()

    # When
    uninstaller = PluginUninstaller(repository=repository)

    # Then
    with pytest.raises(Exception) as format_err:
        uninstaller(options)
