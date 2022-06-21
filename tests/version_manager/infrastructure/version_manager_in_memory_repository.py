from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class VersionManagerInMemoryRepository(VersionManagerRepository):
    VERSIONS_INSTALLED = []

    def list_versions(self, limit: int) -> List[TutorVersion]:
        pass

    @staticmethod
    def local_versions(tvm_path: str) -> List[TutorVersion]:
        pass

    @staticmethod
    def current_version(tvm_path: str) -> List[TutorVersion]:
        pass

    def install_version(self, version: TutorVersion) -> None:
        self.VERSIONS_INSTALLED.append(version)

    def find_version(self, version: TutorVersion) -> Optional[TutorVersion]:
        return version if version in self.VERSIONS_INSTALLED else None

    def uninstall_version(self, version: TutorVersion) -> None:
        pass

    def use_version(self, version: TutorVersion) -> None:
        pass

    @staticmethod
    def version_is_installed(version: str) -> None:
        pass

    def install_plugin(self, options: List) -> None:
        pass

    def uninstall_plugin(self, options: List) -> None:
        pass
