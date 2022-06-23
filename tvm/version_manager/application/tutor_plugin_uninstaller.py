"""Tutor plugin uninstaller application."""
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorPluginUninstaller:
    """Tutor plugin uninstaller for version manager."""

    def __init__(self, repository: VersionManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, options) -> None:
        """call."""
        self.repository.uninstall_plugin(options)
