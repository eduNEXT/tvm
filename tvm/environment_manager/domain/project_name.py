import re

from tvm.environment_manager.domain.project_name_format_error import ProjectNameFormatError


class ProjectName(str):

    def __init__(self, value: str):  # pylint: disable=super-init-not-called
        """Raise BadParameter if the value is not a project name."""
        self._value = value

        result = re.match(r"^v([0-9]+)\.([0-9]+)\.([0-9]+)\@[a-zA-Z0-9]+$", value)
        if not result:
            raise ProjectNameFormatError("format must be 'vX.Y.Z@project_name'")
