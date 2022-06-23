from tests.version_manager.infrastructure.version_manager_in_memory_repository import (
    VersionManagerInMemoryRepository,
)
from tvm.version_manager.application.tutor_version_uninstaller import (
    TutorVersionUninstaller,
)


def test_should_uninstall_the_tutor_version():
    # Given
    version = "v1.2.4"
    repository = VersionManagerInMemoryRepository()

    # When
    uninstaller = TutorVersionUninstaller(repository=repository)
    uninstaller(version=version)

    # Then
    assert version not in repository.VERSIONS_INSTALLED
