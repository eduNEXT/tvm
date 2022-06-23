"""Tutor version application."""
from typing import List

from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorVersionLister:
    """Tutor version lister for version manage."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, limit: int) -> List[TutorVersion]:
        """call."""
        return self.repository.list_versions(limit=limit)
