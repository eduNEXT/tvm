import abc
from abc import abstractmethod


class ClientLoggerRepository(abc.ABC):

    @abstractmethod
    def echo(self, message) -> None:
        pass
