# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import bot
from database.users import store_user_data, store_group_data
from database.user_language import get_user_language
from utils.language import get_message
from utils.inline_buttons import start_buttons
from config import LOG_CHANNEL

@bot.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    chat = message.chat
    store_user_data(user.id, user.username, user.full_name)

    if chat.type in ["group", "supergroup"]:
        store_group_data(chat.id, chat.title)

    lang = get_user_language(user.id)
    welcome_message = get_message(lang, "welcome_message")

    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=welcome_message,
            reply_markup=start_buttons()
        )
    except:
        await message.reply(welcome_message, reply_markup=start_buttons())

    await bot.send_message(LOG_CHANNEL, f"#START by [{user.first_name}](tg://user?id={user.id}) | `{user.id}`")
