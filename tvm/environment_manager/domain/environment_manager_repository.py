"""Environment manager repository methods."""
from abc import ABC, abstractmethod
from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion


class EnvironmentManagerRepository(ABC):
    """Administrate environment manager repository methods."""

    @staticmethod
    @abstractmethod
    def project_init(self, version) -> None:
        """Tutor Project Init to environment manager."""

    @abstractmethod
    def current_version(self) -> None:
        """Get the project's version"""

    @abstractmethod
    def install_plugin(self, options: List) -> None:
        """Install a pip package"""

    @abstractmethod
    def uninstall_plugin(self, options: List) -> None:
        """Uninstall a pip package"""
