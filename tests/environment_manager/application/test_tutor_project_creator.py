import pytest

from tests.environment_manager.infrastructure.environment_manager_in_memory_repository import (
    EnvironmentManagerInMemoryRepository,
)
from tvm.environment_manager.application.tutor_project_creator import (
    TutorProjectCreator,
)


def test_should_create_tutor_project():
    # Given
    project_name = "v13.1.0@testtutor"
    repository = EnvironmentManagerInMemoryRepository()

    # When
    inicialize = TutorProjectCreator(repository=repository)
    inicialize(project_name)

    # Then
    assert project_name in repository.PROJECT_NAME


def test_should_fail_if_project_name_exists():
    # Given
    project_name = "v13.1.0@tutortest"
    repository = EnvironmentManagerInMemoryRepository()

    # When
    inicialize = TutorProjectCreator(repository=repository)

    # Then
    with pytest.raises(Exception) as format_err:
        inicialize(project_name)
