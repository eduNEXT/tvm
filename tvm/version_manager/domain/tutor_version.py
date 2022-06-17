import re
from tvm.version_manager.domain.tutor_version_format_error import (
    TutorVersionFormatError,
)


class TutorVersion(str):
    def __init__(self, value: str, file_url: str = None):
        """Raise BadParameter if the value is not a tutor version."""
        self._value = value
        self._file_url = file_url

        result = re.match(r'^v([0-9]+)\.([0-9]+)\.([0-9]+)$', value)
        if not result:
            raise TutorVersionFormatError("format must be 'vX.Y.Z'")
