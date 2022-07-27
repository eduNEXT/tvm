"""Environment manager repository methods."""
from abc import ABC, abstractmethod
from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion


class EnvironmentManagerRepository(ABC):
    """Administrate environment manager repository methods."""

    @staticmethod
    @abstractmethod
    def project_init(self, version, tvm_project_folder) -> None:
        """Tutor Project Init to environment manager."""
