from typing import List, Optional

from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import (
    VersionManagerRepository,
)


class VersionManagerInMemoryRepository(VersionManagerRepository):
    VERSIONS_INSTALLED = ["v1.2.4"]
    PLUGINS_INSTALLED = ["codejail"]
    LIST_VERSIONS = []
    for version in range(20):
        LIST_VERSIONS.append(f"v1.2.{version}")

    def list_versions(self, limit: int) -> List[TutorVersion]:
        return self.LIST_VERSIONS[0:limit]

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
        if version in self.VERSIONS_INSTALLED:
            self.VERSIONS_INSTALLED.clear()

    def use_version(self, version: TutorVersion) -> None:
        self.VERSIONS_INSTALLED[0] = version

    @staticmethod
    def version_is_installed(version: str) -> None:
        pass

    def install_plugin(self, options: List, version: str = None) -> None:
        if options:
            self.PLUGINS_INSTALLED.append(options)
        else:
            raise Exception(f"Error running venv commands: None")

    def uninstall_plugin(self, options: List, version: str = None) -> None:
        if options == self.PLUGINS_INSTALLED[0]:
            self.PLUGINS_INSTALLED.clear()
        else:
            raise Exception(f"Error running venv commands: None")
