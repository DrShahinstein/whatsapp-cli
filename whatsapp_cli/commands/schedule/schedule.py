from ...prelude.schedule.remove_schedule import remove_schedule
from ...prelude.schedule.sort_schedules import sort_schedules
import click
import webbrowser
import threading
import json
import pyautogui
import time
from datetime import timedelta


def send_message(schedule):
    url = 'https://web.whatsapp.com/send?phone=' + \
        schedule["receiver"] + '&text=' + schedule["message"]
    webbrowser.open(url)
    timer = threading.Timer(10, lambda: pyautogui.press("enter"))
    timer.run()
    remove_schedule(schedule["name"])


@click.command()
def schedule():
    """Schedule your messages"""

    with open("./whatsapp_cli/.config/schedules.json", "r") as f:
        schedules = sort_schedules(json.load(f))

    if not schedules:
        click.echo("No schedules.")

    for schedule in schedules:
        schedule_name = schedule["name"]

        # Current time
        localtime = time.localtime()
        current_hours = localtime.tm_hour
        current_minutes = localtime.tm_min
        current_seconds = localtime.tm_sec
        current_time = current_hours * 3600 + current_minutes * 60 + current_seconds

        # Delivery time
        delivery_time = int(schedule["hours"]) * \
            3600 + int(schedule["minutes"]) * 60
        interval = delivery_time - current_time

        if interval <= 0:
            click.echo("The delivery time of the {} is passed.".format(
                schedule_name))
            remove_schedule(schedule_name)

        else:
            # Send
            human_readable_time = click.style(
                timedelta(seconds=interval), fg="yellow")
            click.echo(
                f"Next message will be delivered in {human_readable_time}")
            timer = threading.Timer(interval, send_message, args=[schedule])
            timer.run()
