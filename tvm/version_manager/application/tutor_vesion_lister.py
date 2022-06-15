from typing import List
from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import (
    VersionManagerRepository,
)


class TutorVersionLister:
    def __init__(self, repository: VersionManagerRepository) -> None:
        self.repository = repository

    def __call__(self, limit: int) -> List[TutorVersion]:
        return self.repository.list_versions(limit=limit)
