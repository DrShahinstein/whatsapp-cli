import json
from ..config import SCHEDULES_PATH


def remove_schedule(schedule_name, path=SCHEDULES_PATH):
    with open(path, "r") as f:
        schedules = json.load(f)

    for index, schedule in enumerate(schedules):
        if schedule["name"] == schedule_name:
            schedules.pop(index)
            with open(path, "w") as f:
                json.dump(schedules, f)
            return True
    return False
