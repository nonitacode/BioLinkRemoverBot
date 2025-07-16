import yaml
import os

def get_message(lang, key):
    try:
        path = f"languages/{lang}.yml"
        if not os.path.exists(path):
            path = "languages/en.yml"
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get(key, f"❗ Missing: {key}")
    except Exception as e:
        return f"❗ Error loading language: {str(e)}"
