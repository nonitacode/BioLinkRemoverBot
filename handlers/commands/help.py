# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.user_language import get_user_language
from utils.language import get_message
from utils.inline_buttons import commands_buttons
from config import LOG_CHANNEL

@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")

    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=help_text,
            reply_markup=commands_buttons()
        )
    except:
        await message.reply(help_text, reply_markup=commands_buttons())

    await app.send_message(
        LOG_CHANNEL,
        f"#HELP used by [{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    )
