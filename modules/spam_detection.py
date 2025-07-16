# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import bot
from database.violation_db import log_violation

SPAM_KEYWORDS = ["http", "t.me", "@", "promo", "buy", "sale", ".com", ".org"]

@bot.on_message(filters.text & ~filters.command)
async def scan_spam_and_links(client, message: Message):
    text = message.text.lower()
    if any(keyword in text for keyword in SPAM_KEYWORDS):
        try:
            await message.delete()
            log_violation(message.from_user.id, "Spam/Bio detected")
            await message.reply("⚠️ Message deleted: suspicious content.")
        except:
            pass

