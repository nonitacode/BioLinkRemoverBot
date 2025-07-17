import yaml
import os

LANGUAGE_DIR = "languages"

def get_message(lang_code: str, key: str) -> str:
    path = os.path.join(LANGUAGE_DIR, f"{lang_code}.yml")
    if not os.path.exists(path):
        path = os.path.join(LANGUAGE_DIR, "en.yml")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get(key, f"⚠️ Missing translation for: {key}")
    except:
        return "⚠️ Language load failed."
