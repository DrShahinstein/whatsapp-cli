import json


def create_schedule(path="./whatsapp_cli/.config/schedules.json", **kwargs):
    with open(path, "r") as f:
        current_json_content = json.load(f)

    with open(path, "w") as f:
        current_json_content.append(kwargs)
        json.dump(current_json_content, f)
