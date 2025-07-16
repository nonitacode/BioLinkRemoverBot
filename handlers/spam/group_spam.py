# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from utils.spam_checker import is_spam, check_and_handle_violation

@app.on_message(filters.text & filters.group)
async def group_text_check(client, message: Message):
    if is_spam(message.text):
        await check_and_handle_violation(message)
