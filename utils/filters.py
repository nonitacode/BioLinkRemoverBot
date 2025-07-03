import re

link_pattern = re.compile(r"(http|https|t\.me|@|\.\w{2,})")

def contains_link(text: str) -> bool:
    return bool(link_pattern.search(text or ""))
