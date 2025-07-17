# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from config import OWNER_ID
from utils.spam_checker import is_spam, check_and_handle_violation

@app.on_message(filters.text & filters.private)
async def private_text_check(client, message: Message):
    user = message.from_user
    if not user or user.is_bot:
        return

    # Skip for OWNER
    if user.id == OWNER_ID:
        return

    if is_spam(message.text):
        await check_and_handle_violation(client, message)
