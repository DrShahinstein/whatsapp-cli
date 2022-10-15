import click
import json
from ...prelude.config import SCHEDULES_PATH, EMPTY_ARRAY


@click.command()
def schedules():
    with open(SCHEDULES_PATH, "w") as f:
        json.dump(EMPTY_ARRAY, f)
