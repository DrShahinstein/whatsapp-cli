import click
from .commands.schedule.create_schedule import schedule as create_schedule
from .commands.schedule.remove_schedule import schedule as remove_schedule
from .commands.schedule.schedule import schedule
from .commands.schedule.reset_schedules import schedules as reset_schedules
from .commands.schedule.list import schedules as list_schedules
from .prelude import initialize_config


@click.group()
def cli(): pass


@cli.group()
def create():
    """A command group for create operations."""


@cli.group()
def remove():
    """A command group for remove operations."""


@cli.group()
def reset():
    """A command group for reset operations."""


@cli.group()
def list():
    """A command group for list operations."""


def main():
    initialize_config.init()
    cli.add_command(schedule)
    create.add_command(create_schedule)
    remove.add_command(remove_schedule)
    reset.add_command(reset_schedules)
    list.add_command(list_schedules)
    cli()


if __name__ == "__main__":
    main()
