"""Tutor project initialize."""
from tvm.environment_manager.domain.environment_manager_repository import EnvironmentManagerRepository


class TutorProjectRemover:
    """Tutor project initialize for environment manager."""

    def __init__(self, repository: EnvironmentManagerRepository) -> None:
        """init."""
        self.repository = repository

    def __call__(self) -> None:
        """call."""
        self.repository.project_remover()
