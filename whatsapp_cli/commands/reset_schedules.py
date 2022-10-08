import click


@click.command()
def schedules():
    f = open("./whatsapp_cli/.config/schedules.json", "w")
    f.close()
