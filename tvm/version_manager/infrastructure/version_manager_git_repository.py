import json
import os
import pathlib
from typing import List

import requests
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import (
    VersionManagerRepository,
)


class VersionManagerGitRepository(VersionManagerRepository):
    VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"
    TVM_PATH = pathlib.Path.home() / ".tvm"

    def get_version_from_api(self, limit: int = 10):
        api_info = requests.get(f"{self.VERSIONS_URL}?per_page={limit}").json()
        return api_info

    def list_versions(self) -> List[TutorVersion]:
        api_info = self.get_version_from_api()
        return [TutorVersion(x.get("name")) for x in api_info]

    def get_tutor_local_versions(self):
        """Return a list of strings with the local version installed. If None, returns empty array."""
        if os.path.exists(f"{self.TVM_PATH}"):
            return [
                x
                for x in os.listdir(f"{self.TVM_PATH}")
                if os.path.isdir(f"{self.TVM_PATH}/{x}")
            ]
        return []

    def get_active_tutor_version(self) -> str:
        """Read the current active version from the json/bash switcher."""
        info_file_path = f"{self.TVM_PATH}/current_bin.json"
        if os.path.exists(info_file_path):
            with open(info_file_path, "r", encoding="utf-8") as info_file:
                data = json.load(info_file)
            return data.get("version", "Invalid active version")
        return "No active version installed"

    def get_project_tutor_version(self, tvm_project_path) -> str:
        """Read the current active version from the json/bash switcher."""
        info_file_path = f"{tvm_project_path}/config.json"
        with open(info_file_path, "r", encoding="utf-8") as info_file:
            data = json.load(info_file)
        return data.get("version")
