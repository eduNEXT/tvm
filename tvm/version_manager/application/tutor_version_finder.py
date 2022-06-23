"""Tutor version finder application."""
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorVersionFinder:
    """Tutor version finder for version manager."""

    def __init__(self, repository: VersionManagerRepository):
        """init."""
        self.repository = repository

    def __call__(self, version: str) -> TutorVersion:
        """call."""
        version = TutorVersion(version)
        return self.repository.find_version(version=version)
