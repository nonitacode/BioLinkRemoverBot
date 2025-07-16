# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import filters
from bot.bot import bot
from modules.inline import commands_buttons
from database.user_language_db import get_user_language
from utils.language import get_message

@bot.on_message(filters.command("help"))
async def help(client, message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")

    await message.reply(
        text=help_text,
        reply_markup=commands_buttons()
    )
