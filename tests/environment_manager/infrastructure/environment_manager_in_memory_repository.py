from typing import List

from tvm.environment_manager.domain.project_name import ProjectName
from tvm.environment_manager.domain.environment_manager_repository import (
    EnvironmentManagerRepository,
)


class EnvironmentManagerInMemoryRepository(EnvironmentManagerRepository):
    PLUGINS_INSTALLED = ["codejail"]
    PROJECT_NAME = ["v13.1.0@tutortest"]

    def project_creator(self, version: str) -> None:
        if version not in self.PROJECT_NAME:
            self.PROJECT_NAME.append(version)
        else:
            raise Exception('There is already a project initiated.')


    def install_plugin(self, options: List) -> None:
        if options:
            self.PLUGINS_INSTALLED.append(options)
        else:
            raise Exception(f"Error running venv commands: None")

    def uninstall_plugin(self, options: List) -> None:
        if options == self.PLUGINS_INSTALLED[0]:
            self.PLUGINS_INSTALLED.clear()
        else:
            raise Exception(f"Error running venv commands: None")

    @staticmethod
    def current_version(self) -> None:
        pass
