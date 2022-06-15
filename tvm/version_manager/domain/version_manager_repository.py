from abc import ABC, abstractmethod
from typing import List

from tvm.version_manager.domain.tutor_version import TutorVersion


class VersionManagerRepository(ABC):
    @abstractmethod
    def list_versions(self) -> List[TutorVersion]:
        pass

    @staticmethod
    @abstractmethod
    def local_versions(tvm_path: str) -> List[TutorVersion]:
        pass

    @staticmethod
    @abstractmethod
    def current_version(tvm_path: str) -> List[TutorVersion]:
        pass
