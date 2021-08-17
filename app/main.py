import click
from .commands import greet
from dotenv import load_dotenv

load_dotenv()

class Base:
    def __init__(self, name: str='Jimmy'):
        self.name = name

@click.group()
@click.pass_context
def cli(ctx):
    """Main group of commands."""
    ctx.obj = Base()

cli.add_command(greet)