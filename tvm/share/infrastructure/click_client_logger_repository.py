import click

from tvm.share.domain.client_logger_repository import ClientLoggerRepository


class ClickClientLoggerRepository(ClientLoggerRepository):

    def echo(self, message) -> None:
        click.echo(click.style(message, fg="yellow"))
