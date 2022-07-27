"""Actions to initialize a project."""
from distutils.dir_util import copy_tree
import json
import os
import pathlib
import shutil
import stat
import subprocess
from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


from tvm.templates.tutor_switcher import TUTOR_SWITCHER_TEMPLATE
from tvm.templates.tvm_activate import TVM_ACTIVATE_SCRIPT

TVM_PATH = pathlib.Path.home() / '.tvm'


class EnvironmentManagerGitRepository(EnvironmentManagerRepository):
    """Principals commands to manage TVM."""

    def project_init(self, version: str, tvm_project_folder: str) -> None:
        """Initialize tutor project."""
        tvm_environment = tvm_project_folder / '.tvm'
        data = {
            "version": f"{version}",
            "tutor_root": f"{tvm_project_folder}",
            "tutor_plugins_root": f"{tvm_project_folder}/plugins"
        }
        context = {
            'version': data.get('version', None),
            'tvm': f"{TVM_PATH}",
        }

        self.create_config_json(tvm_environment, data)
        self.create_active_script(tvm_environment, data)
        self.create_tutor_switcher(tvm_environment, context)
        self.create_project(version)

    def create_config_json(self, tvm_environment: str, data: dict) -> None:
        """Create configuration json file"""
        tvm_project_config_file = f"{tvm_environment}/config.json"
        with open(tvm_project_config_file, 'w', encoding='utf-8') as info_file:
            json.dump(data, info_file, indent=4)

    def create_active_script(self, tvm_environment: str, context: dict) -> None:
        """Create active script file."""
        activate_script = f"{tvm_environment}/bin/activate"
        with open(activate_script, 'w', encoding='utf-8') as activate_file:
            activate_file.write(TVM_ACTIVATE_SCRIPT.render(**context))

    def create_tutor_switcher(self, tvm_environment: str, context: dict) -> None:
        """Create tutor switcher file."""
        tutor_file = f"{tvm_environment}/bin/tutor"
        with open(tutor_file, 'w', encoding='utf-8') as switcher_file:
            switcher_file.write(TUTOR_SWITCHER_TEMPLATE.render(**context))
        # set execute permissions
        os.chmod(tutor_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

    def create_project(self, project: str) -> None:
        """Duplicate the version directory and rename it."""
        if not os.path.exists(f"{TVM_PATH}/{project}"):
            tutor_version = project.split("@")[0]
            tutor_version_folder = f"{TVM_PATH}/{tutor_version}"

            tvm_project = f"{TVM_PATH}/{project}"
            copy_tree(tutor_version_folder, tvm_project)

            shutil.rmtree(f"{tvm_project}/venv")
            self.setup_version_virtualenv(project)

    def setup_version_virtualenv(self, version=None) -> None:
        """Create virtualenv and install tutor cloned."""
        # Create virtualenv
        subprocess.run(f'cd {TVM_PATH}/{version}; virtualenv venv',
                    shell=True, check=True,
                    executable='/bin/bash')

        # Install tutor
        subprocess.run(f'source {TVM_PATH}/{version}/venv/bin/activate;'
                    f'pip install -e {TVM_PATH}/{version}/overhangio-tutor-*/',
                    shell=True, check=True,
                    executable='/bin/bash')
