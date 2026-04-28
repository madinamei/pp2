import json
import os

FILE = "settings.json"

def load_settings():
    if not os.path.exists(FILE):
        data = {"snake_color": [0,200,0], "grid": True, "sound": True}
        save_settings(data)
        return data

    with open(FILE) as f:
        return json.load(f)


def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)