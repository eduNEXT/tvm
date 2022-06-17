from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginUninstaller:
    def __init__(self, repository: VersionManagerRepository) -> None:
        self.repository = repository

    def __call__(self, options) -> None:
        self.repository.uninstall_plugin(options)
