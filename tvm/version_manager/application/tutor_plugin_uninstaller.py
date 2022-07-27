"""Tutor plugin uninstaller application."""
from typing import List

from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginUninstaller:
    """Tutor plugin uninstaller for version manager."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, options: List, version: str = None) -> None:
        """call."""
        if version:
            version = TutorVersion(version=version)
        self.repository.uninstall_plugin(options=options, version=version)
