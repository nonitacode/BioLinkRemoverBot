

import yaml
import os

def get_message(lang: str, key: str):
    try:
        path = f"languages/{lang}.yml"
        if not os.path.exists(path):
            path = "languages/en.yml"
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data.get(key, f"⚠️ Missing translation for key: {key}")
    except Exception as e:
        return f"❌ Language Error: {str(e)}"
