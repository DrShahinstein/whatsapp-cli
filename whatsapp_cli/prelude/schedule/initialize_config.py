import os
import json

CONFIG_PATH = "./whatsapp_cli/.config"
SCHEDULES_CONFIG_PATH = f"{CONFIG_PATH}/schedules.json"
EMPTY_ARRAY_CONFIG = []


def init():
    if not os.path.isdir(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)

    # schedules.json
    if not os.path.isfile(SCHEDULES_CONFIG_PATH):
        with open(SCHEDULES_CONFIG_PATH, "w") as f:
            json.dump(EMPTY_ARRAY_CONFIG, f)
    else:
        with open(SCHEDULES_CONFIG_PATH, "r+") as f:
            if not f.read():
                json.dump(EMPTY_ARRAY_CONFIG, f)
