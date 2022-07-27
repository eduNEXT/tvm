"""Tutor project initialize."""
from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


class TutorProjectInit:
    """Tutor project init for environment manager."""

    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self, version, tvm_project_folder) -> None:
        """call."""
        self.repository.project_init(version, tvm_project_folder)
