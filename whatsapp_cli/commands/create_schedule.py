import click
from ..prelude.schedule.create_schedule import create_schedule
from ..prelude.schedule.is_valid import is_valid_time


@click.command()
def schedule():
    """Create a new schedule"""
    schedule_name = click.prompt("The name of your schedule")
    message = click.prompt("Message")
    receiver = click.prompt("Receiving phone number")
    hours = click.prompt(click.style("hh", fg="bright_red") + ":mm")
    minutes = click.prompt("hh:" + click.style("mm", fg="bright_red"))

    if is_valid_time(hours, minutes) and int(minutes) <= 60:
        create_schedule(name=schedule_name,
                        message=message, receiver=receiver,
                        hours=hours, minutes=minutes)
        click.echo("New schedule created.")
    else:
        click.echo("Not valid time.")
