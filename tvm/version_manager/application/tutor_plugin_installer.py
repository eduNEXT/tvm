from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginInstaller:
    def __init__(self, repository: VersionManagerRepository) -> None:
        self.repository = repository

    def __call__(self, options) -> None:
        self.repository.install_plugin(options)
