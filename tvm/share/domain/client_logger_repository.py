"""Domain clien logger repository."""
import abc
from abc import abstractmethod


class ClientLoggerRepository(abc.ABC):
    """Clien logger."""

    @abstractmethod
    def echo(self, message) -> None:
        """Echo a message."""
