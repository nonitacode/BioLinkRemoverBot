# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.user_language import get_user_language
from utils.language import get_message
from utils.inline_buttons import commands_buttons
from config import LOG_CHANNEL, START_IMG

@app.on_message(filters.command("help") & ~filters.channel)
async def help_command(client, message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    help_text = get_message(lang, "help_message")

    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=help_text,
            reply_markup=await commands_buttons(user_id)
        )
    except:
        await message.reply(
            text=help_text,
            reply_markup=await commands_buttons(user_id)
        )

    await app.send_message(
        LOG_CHANNEL,
        f"#HELP used by [{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    )
