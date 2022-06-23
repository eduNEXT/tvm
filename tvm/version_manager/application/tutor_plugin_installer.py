"""Tutor plugin installer application."""
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginInstaller:
    """Tutor plugin installer for version manager."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, options) -> None:
        """call."""
        self.repository.install_plugin(options)
