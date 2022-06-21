import pytest

from tests.version_manager.infrastructure.version_manager_in_memory_repository import VersionManagerInMemoryRepository
from tvm.version_manager.application.tutor_version_installer import TutorVersionInstaller
from tvm.version_manager.domain.tutor_version_format_error import TutorVersionFormatError


def test_should_fail_if_version_format_is_not_valid():
    # Given
    version = "v123"
    repository = VersionManagerInMemoryRepository()

    # When
    installer = TutorVersionInstaller(repository=repository)

    # Then
    with pytest.raises(TutorVersionFormatError) as format_err:
        installer(version=version)


def test_should_install_the_tutor_version():
    # Given
    version = "v1.2.3"
    repository = VersionManagerInMemoryRepository()

    # When
    installer = TutorVersionInstaller(repository=repository)
    installer(version=version)

    # Then
    assert version in repository.VERSIONS_INSTALLED
