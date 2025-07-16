# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from modules.inline import start_buttons
from config import BOT_NAME
from bot.bot import bot
from database.users_db import store_user_data
from database.user_language_db import get_user_language
from utils.language import get_message

@bot.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    lang = get_user_language(user.id)
    welcome_text = get_message(lang, "welcome_message")
    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=welcome_text,
            reply_markup=start_buttons()
        )
    except:
        await message.reply(welcome_text, reply_markup=start_buttons())
