"""Version manager repository methods."""
from abc import ABC, abstractmethod
from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion


class VersionManagerRepository(ABC):
    """Administrate version manager repository methods."""

    @abstractmethod
    def list_versions(self, limit: int) -> List[TutorVersion]:
        """List versions of the version manager."""

    @staticmethod
    @abstractmethod
    def local_versions(tvm_path: str) -> List[TutorVersion]:
        """List local versions of the version manager."""

    @staticmethod
    @abstractmethod
    def current_version(tvm_path: str) -> List[TutorVersion]:
        """Present the current version of the version manager."""

    @abstractmethod
    def install_version(self, version: TutorVersion) -> None:
        """Install the version manager for tutor version."""

    @abstractmethod
    def find_version(self, version: TutorVersion) -> Optional[TutorVersion]:
        """Find the tutor version manager."""

    @abstractmethod
    def uninstall_version(self, version: TutorVersion) -> None:
        """Uninstall the version manager for tutor version selected."""

    @abstractmethod
    def use_version(self, version: TutorVersion) -> None:
        """Use selected version when is installed."""

    @staticmethod
    @abstractmethod
    def version_is_installed(version: str) -> None:
        """Version is installed method."""

    @abstractmethod
    def install_plugin(self, options: List, version: TutorVersion = None) -> None:
        """Install tutor plugin."""

    @abstractmethod
    def uninstall_plugin(self, options: List, version: TutorVersion = None) -> None:
        """Uninstall tutor plugin."""
