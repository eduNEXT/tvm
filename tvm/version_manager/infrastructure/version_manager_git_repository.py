"Actions to get tutor versions"
import json
import os
from typing import List, Optional

import requests
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import (
    VersionManagerRepository,
)


class VersionManagerGitRepository(VersionManagerRepository):
    "Principals commands to manage TVM"

    VERSIONS_URL = "https://api.github.com/repos/overhangio/tutor/tags"

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
