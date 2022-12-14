import json
from ..config import SCHEDULES_PATH


def create_schedule(path=SCHEDULES_PATH, **kwargs):
    with open(path, "r") as f:
        current_json_content = json.load(f)

    with open(path, "w") as f:
        current_json_content.append(kwargs)
        json.dump(current_json_content, f)
