import json
import os
CONFIG_PATH = "config/settings.json"
def load_settings():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {"default_project": "DefaultProject", "version": "7.9"}
def save_settings(settings):
    os.makedirs("config", exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(settings, f, indent=2)
def update_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)
    return settings
def get_default_project():
    return load_settings().get("default_project", "DefaultProject")
