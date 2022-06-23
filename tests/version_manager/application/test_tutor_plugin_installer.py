import pytest

from tests.version_manager.infrastructure.version_manager_in_memory_repository import (
    VersionManagerInMemoryRepository,
)
from tvm.version_manager.application.tutor_plugin_installer import TutorPluginInstaller


def test_should_install_the_tutor_plugin():
    # Given
    options = ["tutor-mfe"]
    repository = VersionManagerInMemoryRepository()

    # When
    installer = TutorPluginInstaller(repository=repository)
    installer(options)

    # Then
    assert options in repository.PLUGINS_INSTALLED


def test_should_fail_if_not_add_tutor_plugin():
    # Given
    options = []
    repository = VersionManagerInMemoryRepository()

    # When
    installer = TutorPluginInstaller(repository=repository)

    # Then
    with pytest.raises(Exception) as format_err:
        installer(options)
