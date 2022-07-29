"""Actions to get tutor versions."""
import json
import os
import pathlib
import shutil
import stat
import subprocess
import zipfile
from datetime import timedelta
from typing import List, Optional

import requests
import requests_cache

from tvm.share.domain.client_logger_repository import ClientLoggerRepository
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.tutor_version_is_not_installed import TutorVersionIsNotInstalled
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository
from tvm.version_manager.templates.tutor_switcher import TUTOR_SWITCHER_TEMPLATE


class VersionManagerGitRepository(VersionManagerRepository):
    """Principals commands to manage TVM."""

    VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
    GET_TAG_URL = "https://api.github.com/repos/overhangio/tutor/git/ref/tags/"
    ZIPPBALL_URL = "https://api.github.com/repos/overhangio/tutor/zipball/refs/tags/"
    TVM_PATH = pathlib.Path.home() / ".tvm"

    def __init__(self, logger: ClientLoggerRepository) -> None:
        """init."""
        self.logger = logger
        self.setup()

    def setup(self):
        """Set data."""
        try:
            os.mkdir(self.TVM_PATH)
        except FileExistsError:
            pass

        data = {
            "version": None,
            "tutor_root": None,
            "tutor_plugins_root": None,
        }

        self.set_current_info(data=data, update=False)
        self.set_switcher()

        try:
            os.symlink(f"{self.TVM_PATH}/tutor_switcher", "/usr/local/bin/tutor")
        except PermissionError:
            self.logger.echo(
                "Don't Worry, TVM just needs sudo permissions to create the tutor_switcher's symlink"
                "in /usr/local/bin/tutor.\n"
                "You can find more information about it in our docs."
            )
            subprocess.call(
                [
                    "sudo",
                    "ln",
                    "-s",
                    f"{self.TVM_PATH}/tutor_switcher",
                    "/usr/local/bin/tutor",
                ]
            )
        except FileExistsError:
            pass

    def set_current_info(self, data: dict, update: bool = True) -> None:
        """Set current information."""
        try:
            info_file_path = f"{self.TVM_PATH}/current_bin.json"
            if os.path.exists(info_file_path) and not update:
                raise FileExistsError

            with open(info_file_path, "w", encoding="utf-8") as info_file:
                json.dump(data, info_file, indent=4)
        except FileExistsError:
            pass

    def get_current_info(self) -> dict:
        """Get current information data from the json."""
        info_file_path = f"{self.TVM_PATH}/current_bin.json"
        with open(info_file_path, "r", encoding="utf-8") as info_file:
            data = json.load(info_file)
        return data

    def set_switcher(self) -> None:
        """Set the active version from the json into the switcher."""
        data = self.get_current_info()

        context = {
            "version": data.get("version", None),
            "tutor_root": data.get("tutor_root", None),
            "tutor_plugins_root": data.get("tutor_plugins_root", None),
            "tvm": f"{self.TVM_PATH}",
        }

        switcher_file = f"{self.TVM_PATH}/tutor_switcher"
        with open(switcher_file, mode="w", encoding="utf-8") as of_text:
            of_text.write(TUTOR_SWITCHER_TEMPLATE.render(**context))

        # set execute permissions
        os.chmod(
            switcher_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH
        )

    def get_version_from_api(self, limit: int = 100):
        """Return api information form request."""
        requests_cache.install_cache('github_cache', expire_after=timedelta(days=1))
        api_info = requests.get(f"{self.VERSIONS_URL}?per_page={limit}").json()
        return api_info

    def list_versions(self, limit: int) -> List[TutorVersion]:
        """List tutor version from API."""
        api_info = self.get_version_from_api(limit=limit)
        return [TutorVersion(x.get("name")) for x in api_info]

    @staticmethod
    def local_versions(tvm_path: str) -> List[TutorVersion]:
        """Return a list of strings with the local version installed. If None, returns empty array."""
        if os.path.exists(f"{tvm_path}"):
            return [
                x for x in os.listdir(f"{tvm_path}") if os.path.isdir(f"{tvm_path}/{x}")
            ]
        return []

    @staticmethod
    def current_version(tvm_path: str) -> Optional[TutorVersion]:
        """Read the current active version from the json/bash switcher."""
        info_file_path = f"{tvm_path}/current_bin.json"
        if not os.path.exists(info_file_path):
            return None

        with open(info_file_path, "r", encoding="utf-8") as info_file:
            data = json.load(info_file)
        return TutorVersion(data.get("version")) if data.get("version") else None

    def install_version(self, version: TutorVersion) -> None:
        """Install version for a tutor version."""
        # Get the code in zip format
        filename = f"{self.TVM_PATH}/{version}.zip"
        file_url = f"{self.ZIPPBALL_URL}{version}"
        stream = requests.get(file_url, stream=True)
        with open(filename, "wb") as target_file:
            for chunk in stream.iter_content(chunk_size=256):
                target_file.write(chunk)

        # Unzip it
        with zipfile.ZipFile(filename, "r") as ziped:
            ziped.extractall(f"{self.TVM_PATH}/{version}")

        # Delete artifact
        os.remove(filename)

        self.create_virtualenv(version)
        self.install_tutor(version)

    def find_version(self, version: TutorVersion) -> Optional[TutorVersion]:
        """Find version for requests."""
        response = requests.get(f"{self.GET_TAG_URL}{version}")
        if response.status_code == 404:
            return None

        return TutorVersion(version)

    def create_virtualenv(self, version: TutorVersion) -> None:
        """Create a virtual environment."""
        subprocess.run(
            f"cd {self.TVM_PATH}/{version}; virtualenv --prompt {version} venv",
            shell=True,
            check=True,
            executable="/bin/bash",
        )

    def run_command_in_virtualenv(self, options: List, version: TutorVersion = None):  # pylint: duplicate-code
        """Use virtual environment to run command."""
        if not version:
            version = self.current_version(self.TVM_PATH)

        try:
            subprocess.run(
                f"source {self.TVM_PATH}/{version}/venv/bin/activate;" f'pip {" ".join(options)}',
                shell=True,
                check=True,
                executable="/bin/bash",
            )
        except subprocess.CalledProcessError as ex:
            raise Exception(f"Error running venv commands: {ex.output}") from ex

    def install_plugin(self, options: List, version: TutorVersion = None) -> None:
        """Install plugin for virtual environment."""
        self.run_command_in_virtualenv(options)

    def uninstall_plugin(self, options: List, version: TutorVersion = None) -> None:
        """Uninstall plugin for virtual environment."""
        self.run_command_in_virtualenv(options)

    def install_tutor(self, version: TutorVersion) -> None:
        """Install a tutor version."""
        subprocess.run(
            f"source {self.TVM_PATH}/{version}/venv/bin/activate;"
            f"pip install -e {self.TVM_PATH}/{version}/overhangio-tutor-*/",
            shell=True,
            check=True,
            executable="/bin/bash",
        )

    def uninstall_version(self, version: TutorVersion) -> None:
        """Uninstall a tutor version."""
        try:
            shutil.rmtree(f"{self.TVM_PATH}/{version}")
        except FileNotFoundError as v_not_exist:
            raise TutorVersionIsNotInstalled(
                f"The version {version} is not installed"
            ) from v_not_exist

    def use_version(self, version: TutorVersion) -> None:
        """Use a tutor version selected."""
        data = self.get_current_info()

        data.update({"version": version})

        self.set_current_info(data=data)
        self.set_switcher()

    @staticmethod
    def version_is_installed(version: str) -> bool:
        """Validate if tutor version is installed."""
        version = TutorVersion(version)
        if not os.path.exists(f"{VersionManagerGitRepository.TVM_PATH}/{version}"):
            return False
        return True
