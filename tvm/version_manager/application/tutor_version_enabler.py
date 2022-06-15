from tvm.version_manager.domain.tutor_version import TutorVersion
from tvm.version_manager.domain.version_manager_repository import VersionManagerRepository


class TutorVersionEnabler:
    def __init__(self, repository: VersionManagerRepository) -> None:
        self.repository = repository

    def __call__(self, version: str) -> None:
        version = TutorVersion(version)
        self.repository.use_version(version)
