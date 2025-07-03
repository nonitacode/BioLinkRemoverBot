import re
from pyrogram.types import Message

def contains_link(text: str) -> bool:
    link_pattern = re.compile(r"(https?://|www\.)\S+|@\w{5,32}")
    return bool(link_pattern.search(text or ""))

def is_link_message(message: Message) -> bool:
    if message.text and contains_link(message.text):
        return True
    if message.caption and contains_link(message.caption):
        return True
    return False
