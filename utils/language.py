# utils/language.py
import yaml
import os

LANGUAGE_DIR = "language"

def get_message(lang_code: str, key: str) -> str:
    print(f"⚠️ DEBUG: Trying to load lang_code={lang_code}, key={key}")
    path = os.path.join(LANGUAGE_DIR, f"{lang_code}.yml")

    if not os.path.exists(path):
        print(f"⚠️ DEBUG: Fallback to en.yml because {lang_code}.yml not found")
        path = os.path.join(LANGUAGE_DIR, "en.yml")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        print(f"✅ DEBUG: Language loaded: {key} -> {data.get(key)}")
        return data.get(key, f"⚠️ Missing translation for: {key}")
    except Exception as e:
        print(f"❌ LANGUAGE LOAD ERROR: {e}")
        return "⚠️ Language load failed."
