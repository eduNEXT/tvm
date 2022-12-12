import pytest

from tests.environment_manager.infrastructure.environment_manager_in_memory_repository import (
    EnvironmentManagerInMemoryRepository,
)
from tvm.environment_manager.application.tutor_project_remover import (
    TutorProjectRemover,
)


def test_should_remove_tutor_project():
    # Given
    repository = EnvironmentManagerInMemoryRepository()

    # When
    remove = TutorProjectRemover(repository=repository)
    remove()

    # Then
    assert repository.PROJECT_NAME == []
