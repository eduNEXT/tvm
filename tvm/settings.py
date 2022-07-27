from tvm.environment_manager.infrastructure.environment_manager_git_repository import EnvironmentManagerGitRepository
from tvm.share.infrastructure.click_client_logger_repository import ClickClientLoggerRepository
from tvm.version_manager.infrastructure.version_manager_git_repository import VersionManagerGitRepository

logger = ClickClientLoggerRepository()
version_manager = VersionManagerGitRepository(logger=logger)


def environment_manager(project_path: str) -> EnvironmentManagerGitRepository:
    return EnvironmentManagerGitRepository(project_path=project_path)

