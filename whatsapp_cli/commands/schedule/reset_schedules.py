import click
import json

EMPTY_ARRAY_CONFIG = []


@click.command()
def schedules():
    with open("./whatsapp_cli/.config/schedules.json", "w") as f:
        json.dump(EMPTY_ARRAY_CONFIG, f)
