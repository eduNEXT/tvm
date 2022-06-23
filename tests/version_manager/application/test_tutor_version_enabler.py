from tests.version_manager.infrastructure.version_manager_in_memory_repository import (
    VersionManagerInMemoryRepository,
)
from tvm.version_manager.application.tutor_version_enabler import TutorVersionEnabler


def test_should_enabler_the_tutor_version():
    # Given
    version = "v1.2.3"
    repository = VersionManagerInMemoryRepository()

    # When
    enabler = TutorVersionEnabler(repository=repository)
    enabler(version=version)

    # Then
    assert version in repository.VERSIONS_INSTALLED
