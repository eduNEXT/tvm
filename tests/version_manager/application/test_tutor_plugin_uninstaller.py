import pytest

from tests.version_manager.infrastructure.version_manager_in_memory_repository import (
    VersionManagerInMemoryRepository,
)
from tvm.version_manager.application.tutor_plugin_uninstaller import (
    TutorPluginUninstaller,
)


def test_should_uninstall_the_tutor_plugin():
    # Given
    options = "codejail"
    repository = VersionManagerInMemoryRepository()

    # When
    uninstaller = TutorPluginUninstaller(repository=repository)
    uninstaller(options)

    # Then
    assert options not in repository.VERSIONS_INSTALLED


def test_should_fail_if_not_add_tutor_plugin():
    # Given
    options = "tutor-mfe"
    repository = VersionManagerInMemoryRepository()

    # When
    uninstaller = TutorPluginUninstaller(repository=repository)

    # Then
    with pytest.raises(Exception) as format_err:
        uninstaller(options)
