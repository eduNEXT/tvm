from abc import ABC, abstractmethod
from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion


class VersionManagerRepository(ABC):
    @abstractmethod
    def list_versions(self, limit: int) -> List[TutorVersion]:
        pass

    @staticmethod
    @abstractmethod
    def local_versions(tvm_path: str) -> List[TutorVersion]:
        pass

    @staticmethod
    @abstractmethod
    def current_version(tvm_path: str) -> List[TutorVersion]:
        pass

    @abstractmethod
    def install_version(self, version: TutorVersion) -> None:
        pass

    @abstractmethod
    def find_version(self, version: TutorVersion) -> Optional[TutorVersion]:
        pass

    @abstractmethod
    def uninstall_version(self, version: TutorVersion) -> None:
        pass

    @abstractmethod
    def use_version(self, version: TutorVersion) -> None:
        pass

    @staticmethod
    @abstractmethod
    def version_is_installed(version: str) -> None:
        pass

    @abstractmethod
    def install_plugin(self, options: List) -> None:
        pass

    @abstractmethod
    def uninstall_plugin(self, options: List) -> None:
        pass
