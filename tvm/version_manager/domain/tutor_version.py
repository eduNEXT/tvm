import re

from tvm.version_manager.domain.tutor_version_format_error import (
    TutorVersionFormatError,
)


class TutorVersion(str):
    def __init__(self, value):
        """Raise BadParameter if the value is not a tutor version."""

        result = re.match(r"^v([0-9]+)\.([0-9]+)\.([0-9]+)$", value)
        if not result:
            raise TutorVersionFormatError("format must be 'vX.Y.Z'")
