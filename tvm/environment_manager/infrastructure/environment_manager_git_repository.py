"""Actions to initialize a project."""
from distutils.dir_util import copy_tree
import json
import os
import pathlib
import shutil
import stat
import subprocess
from typing import List

from tvm.environment_manager.domain.environment_manager_repository import (
    EnvironmentManagerRepository,
)
from tvm.environment_manager.domain.project_name import ProjectName

from tvm.templates.tutor_switcher import TUTOR_SWITCHER_TEMPLATE
from tvm.templates.tvm_activate import TVM_ACTIVATE_SCRIPT

TVM_PATH = pathlib.Path.home() / ".tvm"


class EnvironmentManagerGitRepository(EnvironmentManagerRepository):
    """Principals commands to manage TVM."""

    def __init__(self, project_path: str) -> None:
        self.PROJECT_PATH = project_path
        self.TVM_ENVIRONMENT = f"{project_path}/.tvm"

    def project_creator(self, version: str) -> None:
        """Initialize tutor project."""
        data = {
            "version": f"{version}",
            "tutor_root": f"{self.PROJECT_PATH}",
            "tutor_plugins_root": f"{self.PROJECT_PATH}/plugins",
        }

        self.create_config_json(data)
        self.create_active_script(data)
        self.create_project(version)

    def current_version(self) -> ProjectName:
        info_file_path = f"{self.TVM_ENVIRONMENT}/config.json"
        with open(info_file_path, "r", encoding="utf-8") as info_file:
            data = json.load(info_file)
        return ProjectName(data.get("version"))

    def create_config_json(self, data: dict) -> None:
        """Create configuration json file"""
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

    def create_project(self, project: str) -> None:
        """Duplicate the version directory and rename it."""
        if not os.path.exists(f"{TVM_PATH}/{project}"):
            tutor_version = project.split("@")[0]
            tutor_version_folder = f"{TVM_PATH}/{tutor_version}"

            tvm_project = f"{TVM_PATH}/{project}"
            copy_tree(tutor_version_folder, tvm_project)

            shutil.rmtree(f"{tvm_project}/venv")
            self.setup_version_virtualenv(project)

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
                shell=True,
                check=True,
                executable="/bin/bash",
            )
        except subprocess.CalledProcessError as ex:
            raise Exception(f"Error running venv commands: {ex.output}") from ex

    def install_plugin(self, options: List) -> None:
        self.run_command_in_virtualenv(options=options)

    def uninstall_plugin(self, options: List) -> None:
        self.run_command_in_virtualenv(options=options)
