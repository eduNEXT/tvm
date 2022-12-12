"""Environment manager repository methods."""
from abc import ABC, abstractmethod
from typing import List

from tvm.environment_manager.domain.project_name import ProjectName


class EnvironmentManagerRepository(ABC):
    """Administrate environment manager repository methods."""

    @abstractmethod
    def project_creator(self, project_name: ProjectName) -> None:
        """Tutor Project Init to environment manager."""

    @abstractmethod
    def project_remover(self) -> None:
        """Tutor Project Remove to environment manager."""

    @abstractmethod
    def current_version(self) -> None:
        """Get the project's version."""

    @abstractmethod
    def install_plugin(self, options: List) -> None:
        """Install a pip package."""

    @abstractmethod
    def uninstall_plugin(self, options: List) -> None:
        """Uninstall a pip package."""
