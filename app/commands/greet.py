import click

@click.command()
@click.option('--name', envvar='GREET_NAME', default='Jimmy')
@click.pass_obj
def greet(ctx, name):
    if name:
        ctx.name = name
    click.echo(f"Hello, World {ctx.name}")