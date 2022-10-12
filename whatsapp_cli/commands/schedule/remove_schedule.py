import click
from ...prelude.schedule.remove_schedule import remove_schedule


@click.command()
def schedule():
    """Remove a schedule"""

    while True:
        schedule_name = click.prompt(
            "Enter the name of the schedule you want to remove")
        valid = remove_schedule(schedule_name)
        colored_schedule_name = click.style(schedule_name, fg="yellow")

        if valid:
            click.echo(f"{colored_schedule_name} removed.")
        else:
            click.echo(f"{colored_schedule_name} not found.")
