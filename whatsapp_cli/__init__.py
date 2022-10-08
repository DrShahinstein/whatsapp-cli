import click
from .commands.create_schedule import schedule as create_schedule
from .commands.remove_schedule import schedule as remove_schedule
from .commands.schedule import schedule
from .commands.reset_schedules import schedules as reset_schedules
from .prelude.schedule import initialize_config


@click.group()
def cli(): pass


@cli.group()
def create(): pass


@cli.group()
def remove(): pass


@cli.group()
def reset(): pass


def main():
    initialize_config.init()
    cli.add_command(schedule)
    create.add_command(create_schedule)
    remove.add_command(remove_schedule)
    reset.add_command(reset_schedules)
    cli()


if __name__ == "__main__":
    main()