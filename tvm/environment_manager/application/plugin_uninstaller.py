from typing import List

from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


class PluginUninstaller:
    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        self.repository = repository

    def __call__(self, options: List) -> None:
        self.repository.uninstall_plugin(options=options)
