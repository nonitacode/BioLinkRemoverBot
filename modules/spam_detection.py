# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.violation_db import log_violation
import re
from bot.bot import bot

SPAM_KEYWORDS = ["http", "@", "promo", "buy", "sale"]

@bot.on_message(filters.text)
async def detect_spam(client, message: Message):
    text = message.text.lower()
    if any(keyword in text for keyword in SPAM_KEYWORDS):
        await message.delete()  # Delete the message
        log_violation(message.from_user.id, "Spam message detected")
        await message.reply("Your message has been deleted due to potential spam.")
