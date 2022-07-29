"""Tutor plugin installer application."""
from typing import List

from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginInstaller:
    """Tutor plugin installer for version manager."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, options: List, version: TutorVersion = None) -> None:
        """call."""
        if version:
            version = TutorVersion(version=version)
        self.repository.install_plugin(options=options, version=version)
