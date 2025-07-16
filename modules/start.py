# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import filters
from bot.bot import bot
from modules.inline import start_buttons
from config import BOT_NAME, LOG_CHANNEL
from database.user_language_db import get_user_language
from utils.language import get_message
from database.users_db import store_user_data
from pyrogram.types import InputMediaPhoto

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)

    lang = get_user_language(user.id)
    welcome = get_message(lang, "welcome_message")

    await message.reply_photo(
        photo="assets/biolinkremoverbot.png",
        caption=welcome,
        reply_markup=start_buttons()
    )

    # Log to LOG_CHANNEL
    await bot.send_message(
        LOG_CHANNEL,
        f"#STARTED\n\n👤 User: {user.mention} (`{user.id}`)\n📩 Started bot in private chat."
    )
