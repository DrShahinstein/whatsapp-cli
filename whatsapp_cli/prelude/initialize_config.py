import os
import json
from .config import CONFIG_PATH, SCHEDULES_PATH, EMPTY_ARRAY


def init():
    if not os.path.isdir(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)

    # schedules.json
    if not os.path.isfile(SCHEDULES_PATH):
        with open(SCHEDULES_PATH, "w") as f:
            json.dump(EMPTY_ARRAY, f)
    else:
        with open(SCHEDULES_PATH, "r+") as f:
            if not f.read():
                json.dump(EMPTY_ARRAY, f)
