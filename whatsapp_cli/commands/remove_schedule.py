import click
from ..prelude.schedule.remove_schedule import remove_schedule


@click.command()
def schedule():
    """Remove a schedule"""

    while True:
        schedule_name = click.prompt(
            "Enter the name of the schedule you want to remove")

        valid = remove_schedule(schedule_name)
        if valid:
            click.echo(f"{schedule_name} removed.")
        else:
            click.echo(f"{schedule_name} not found.")
