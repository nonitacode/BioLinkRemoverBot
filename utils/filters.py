import re

def contains_link(text):
    if not text:
        return False
    return bool(re.search(r"(http[s]?://|t\.me/|@\w+)", text))
