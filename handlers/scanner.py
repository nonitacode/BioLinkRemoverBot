from pyrogram import Client
from pyrogram.types import Message
from filters.suspicious import suspicious_link_filter
from utils.db import is_whitelisted

async def scan_links(client: Client, message: Message):
    if not message.text and not message.caption:
        return

    user_id = message.from_user.id
    chat_id = message.chat.id

    if await is_whitelisted(user_id, chat_id):
        return  # Skip for whitelisted users/groups

    if suspicious_link_filter(message):
        try:
            await message.delete()
        except:
            pass

        try:
            await message.reply_text("⚠️ Suspicious link detected and deleted.")
        except:
            pass
