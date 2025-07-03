import re
from pyrogram.types import Message

# Add more patterns as needed
suspicious_patterns = [
    r"(free|claim).*gift", 
    r"(http|https):\/\/[^\s]+",  # Any link
    r"t\.me\/joinchat\/",        # Telegram invites
    r"(porn|xxx|nude)",          # NSFW terms
    r"(grabify|iplogger)"
]

def suspicious_link_filter(message: Message) -> bool:
    text = message.text or message.caption or ""
    for pattern in suspicious_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False
