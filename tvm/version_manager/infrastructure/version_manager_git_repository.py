"""Actions to get tutor versions"""
import json
import os
import stat
import pathlib
import subprocess
import zipfile
from typing import List, Optional

import requests
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import (
    VersionManagerRepository,
)
from tvm.version_manager.templates.tutor_switcher import TUTOR_SWITCHER_TEMPLATE


class VersionManagerGitRepository(VersionManagerRepository):
    """Principals commands to manage TVM"""

    VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
    GET_TAG_URL = "https://api.github.com/repos/overhangio/tutor/git/ref/tags/"
    ZIPPBALL_URL = "https://api.github.com/repos/overhangio/tutor/zipball/refs/tags/"
    TVM_PATH = pathlib.Path.home() / ".tvm"

    def __init__(self) -> None:
        self.setup()

    def setup(self):
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
            os.symlink(f'{self.TVM_PATH}/tutor_switcher', '/usr/local/bin/tutor')
        except PermissionError:
            subprocess.call(['sudo', 'ln', '-s', f'{self.TVM_PATH}/tutor_switcher', '/usr/local/bin/tutor'])
        except FileExistsError:
            pass

    def set_current_info(self, data: dict, update: bool = True) -> None:
        try:
            info_file_path = f'{self.TVM_PATH}/current_bin.json'
            if os.path.exists(info_file_path) and not update:
                raise FileExistsError

            with open(info_file_path, 'w', encoding='utf-8') as info_file:
                json.dump(data, info_file, indent=4)
        except FileExistsError:
            pass

    def get_current_info(self) -> dict:
        info_file_path = f'{self.TVM_PATH}/current_bin.json'
        with open(info_file_path, 'r', encoding='utf-8') as info_file:
            data = json.load(info_file)
        return data

    def set_switcher(self) -> None:
        """Set the active version from the json into the switcher."""
        data = self.get_current_info()

        context = {
            'version': data.get('version', None),
            'tutor_root': data.get('tutor_root', None),
            'tutor_plugins_root': data.get('tutor_plugins_root', None),
            'tvm': f"{self.TVM_PATH}",
        }

        switcher_file = f'{self.TVM_PATH}/tutor_switcher'
        with open(switcher_file, mode='w', encoding='utf-8') as of_text:
            of_text.write(TUTOR_SWITCHER_TEMPLATE.render(**context))

        # set execute permissions
        os.chmod(switcher_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

    def get_version_from_api(self, limit: int = 10):
        "Return api information form request"

        api_info = requests.get(f"{self.VERSIONS_URL}?per_page={limit}").json()
        return api_info

    def list_versions(self) -> List[TutorVersion]:
        api_info = self.get_version_from_api()
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
        # Get the code in zip format
        filename = f'{self.TVM_PATH}/{version}.zip'
        file_url = f"{self.ZIPPBALL_URL}{version}"
        stream = requests.get(file_url, stream=True)
        with open(filename, 'wb') as target_file:
            for chunk in stream.iter_content(chunk_size=256):
                target_file.write(chunk)

        # Unzip it
        with zipfile.ZipFile(filename, "r") as ziped:
            ziped.extractall(f'{self.TVM_PATH}/{version}')

        # Delete artifact
        os.remove(filename)

        self.create_virtualenv(version)
        self.install_tutor(version)

    def find_version(self, version: TutorVersion) -> Optional[TutorVersion]:
        response = requests.get(f"{self.GET_TAG_URL}{version}")
        if response.status_code == 404:
            return None

        return TutorVersion(version)

    def create_virtualenv(self, version: TutorVersion) -> None:
        subprocess.run(f'cd {self.TVM_PATH}/{version}; virtualenv --prompt {version} venv',
                       shell=True, check=True,
                       executable='/bin/bash')

    def install_tutor(self, version: TutorVersion) -> None:
        subprocess.run(f'source {self.TVM_PATH}/{version}/venv/bin/activate;'
                       f'pip install -e {self.TVM_PATH}/{version}/overhangio-tutor-*/',
                       shell=True, check=True,
                       executable='/bin/bash')
