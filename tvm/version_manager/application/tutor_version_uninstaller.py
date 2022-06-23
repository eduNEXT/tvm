"""Tutor version uninstaller application."""
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorVersionUninstaller:
    """Tutor version uninstaller for version manager."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, version: str) -> None:
        """call."""
        version = TutorVersion(version)
        self.repository.uninstall_version(version)
