import click
import json
from ...prelude.config import SCHEDULES_PATH


def truncate(message: str):
    if len(message) > 40:
        return message[:40] + "..."
    else:
        return message


@click.command()
def schedules():
    """List all schedules."""

    with open(SCHEDULES_PATH, "r") as f:
        schedules = json.load(f)

    if not schedules:
        click.echo("You don't have any schedule.")

    for schedule in schedules:
        name = click.style("{}".format(schedule["name"]), fg="yellow")
        message = truncate(schedule["message"])
        click.echo(f"⸱ {name}: {message}")
