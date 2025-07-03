import re

# Matches URLs, Telegram usernames, domains, etc.
link_pattern = re.compile(
    r"(http[s]?://|t\.me/|@|\.com|\.net|\.org|\.in|\.xyz|\.link|\.me|\.gg|discord\.gg)"
)

def contains_link(text: str) -> bool:
    return bool(link_pattern.search(text or ""))
