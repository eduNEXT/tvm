import pytest

from tests.environment_manager.infrastructure.environment_manager_in_memory_repository import (
    EnvironmentManagerInMemoryRepository,
)
from tvm.environment_manager.application.plugin_installer import PluginInstaller


def test_should_install_the_tutor_plugin():
    # Given
    options = ["tutor-mfe"]
    repository = EnvironmentManagerInMemoryRepository()

    # When
    installer = PluginInstaller(repository=repository)
    installer(options)

    # Then
    assert options in repository.PLUGINS_INSTALLED


def test_should_fail_if_not_add_tutor_plugin():
    # Given
    options = []
    repository = EnvironmentManagerInMemoryRepository()

    # When
    installer = PluginInstaller(repository=repository)

    # Then
    with pytest.raises(Exception) as format_err:
        installer(options)
