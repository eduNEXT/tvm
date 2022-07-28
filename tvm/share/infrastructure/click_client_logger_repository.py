"""Infrastructure click clien logger repository."""
import click

from tvm.share.domain.client_logger_repository import ClientLoggerRepository


class ClickClientLoggerRepository(ClientLoggerRepository):
    """click clien logger repository."""

    def echo(self, message) -> None:
        """Echo message."""
        click.echo(click.style(message, fg="yellow"))
