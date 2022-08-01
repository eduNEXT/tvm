"""Tutor project initialize."""
from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository
from tvm.environment_manager.domain.project_name import ProjectName


class TutorProjectCreator:
    """Tutor project initialize for environment manager."""

    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, version: str) -> None:
        """call."""
        project_name = ProjectName(version)
        self.repository.project_creator(project_name)
