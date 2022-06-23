from tests.version_manager.infrastructure.version_manager_in_memory_repository import (
    VersionManagerInMemoryRepository,
)
from tvm.version_manager.application.tutor_vesion_lister import TutorVersionLister


def test_should_list_tutor_versions():
    # Given
    limit = 10
    list_versions = []
    for version in range(limit):
        list_versions.append(f"v1.2.{version}")
    repository = VersionManagerInMemoryRepository()

    # When
    lister = TutorVersionLister(repository=repository)

    # Then
    assert list_versions == lister(limit=limit)
