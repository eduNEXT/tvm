"""Tutor project initialize."""
from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


class TutorProjectCreator:
    """Tutor project initialize for environment manager."""

    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, version) -> None:
        """call."""
        self.repository.project_creator(version)
