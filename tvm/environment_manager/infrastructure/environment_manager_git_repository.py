"""Actions to initialize a project."""
import json
import os
import pathlib
import shutil
import subprocess
from distutils.dir_util import copy_tree
from typing import List

from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository
from tvm.environment_manager.domain.project_name import ProjectName
from tvm.templates.tvm_activate import TVM_ACTIVATE_SCRIPT

TVM_PATH = pathlib.Path.home() / ".tvm"


class EnvironmentManagerGitRepository(EnvironmentManagerRepository):
    """Principals commands to manage TVM."""

    def __init__(self, project_path: str) -> None:
        """Initialize usefull variables."""
        self.PROJECT_PATH = project_path
        self.TVM_ENVIRONMENT = f"{project_path}/.tvm"

    def project_creator(self, project_name: ProjectName) -> None:
        """Initialize tutor project."""
        data = {
            "version": f"{project_name}",
            "tutor_root": f"{self.PROJECT_PATH}",
            "tutor_plugins_root": f"{self.PROJECT_PATH}/plugins",
        }

        self.create_config_json(data)
        self.create_active_script(data)
        self.create_project(project_name)

    def current_version(self) -> ProjectName:
        """Project name in current version."""
        info_file_path = f"{self.TVM_ENVIRONMENT}/config.json"
        with open(info_file_path, "r", encoding="utf-8") as info_file:
            data = json.load(info_file)
        return ProjectName(data.get("version"))

    def create_config_json(self, data: dict) -> None:
        """Create configuration json file."""
        tvm_project_config_file = f"{self.TVM_ENVIRONMENT}/config.json"
        with open(tvm_project_config_file, "w", encoding="utf-8") as info_file:
            json.dump(data, info_file, indent=4)

    def create_active_script(self, context: dict) -> None:
        """Create active script file."""
        context.update({
            "tvm_path": TVM_PATH
        })
        activate_script = f"{self.TVM_ENVIRONMENT}/bin/activate"
        with open(activate_script, "w", encoding="utf-8") as activate_file:
            activate_file.write(TVM_ACTIVATE_SCRIPT.render(**context))

    def create_project(self, project_name: ProjectName) -> None:
        """Duplicate the version directory and rename it."""
        if not os.path.exists(f"{TVM_PATH}/{project_name}"):
            tutor_version = project_name.split("@")[0]
            tutor_version_folder = f"{TVM_PATH}/{tutor_version}"

            tvm_project = f"{TVM_PATH}/{project_name}"
            copy_tree(tutor_version_folder, tvm_project)

            shutil.rmtree(f"{tvm_project}/venv")
            self.setup_version_virtualenv(project_name)

    @staticmethod
    def setup_version_virtualenv(version=None) -> None:
        """Create virtualenv and install tutor cloned."""
        # Create virtualenv
        subprocess.run(
            f"cd {TVM_PATH}/{version}; virtualenv --prompt {version} venv",
            shell=True,
            check=True,
            executable="/bin/bash",
        )

        # Install tutor
        subprocess.run(
            f"source {TVM_PATH}/{version}/venv/bin/activate;"
            f"pip install -e {TVM_PATH}/{version}/overhangio-tutor-*/",
            shell=True,
            check=True,
            executable="/bin/bash",
        )

    def run_command_in_virtualenv(self, options: List, name: ProjectName = None):
        """Use virtual environment to run command."""
        if not name:
            name = self.current_version()

        try:
            subprocess.run(
                f"source {TVM_PATH}/{name}/venv/bin/activate;"
                f'pip {" ".join(options)}',
                # pylint: disable=duplicate-code
                shell=True,
                check=True,
                executable="/bin/bash",
            )
        except subprocess.CalledProcessError as ex:
            raise Exception(f"Error running venv commands: {ex.output}") from ex

    def install_plugin(self, options: List) -> None:
        """Install a tutor version."""
        self.run_command_in_virtualenv(options=options)

    def uninstall_plugin(self, options: List) -> None:
        """Uninstall a tutor version."""
        self.run_command_in_virtualenv(options=options)
