"""Tutor plugin uninstaller application."""
from typing import List

from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


class PluginUninstaller:
    """Tutor plugin uninstaller for environment manager."""

    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, options: List) -> None:
        """call."""
        self.repository.uninstall_plugin(options=options)
