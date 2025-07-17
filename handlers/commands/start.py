# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.users import store_user_data, get_user_language
from database.groups import store_group_data
from utils.language import get_message
from utils.inline_buttons import start_buttons
from config import LOG_CHANNEL, START_IMG

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    chat = message.chat

    # Store user and group info
    await store_user_data(user.id, user.username, user.full_name)
    if chat.type in ["group", "supergroup"]:
        await store_group_data(chat.id, chat.title)

    # Language selection
    lang = await get_user_language(user.id)
    welcome_message = get_message(lang, "WELCOME").format(user=user.mention)

    # Send welcome image or fallback text
    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=welcome_message,
            reply_markup=await start_buttons(user.id)
        )
    except Exception:
        await message.reply(
            text=welcome_message,
            reply_markup=await start_buttons(user.id)
        )

    # Log to log channel
    await app.send_message(
        LOG_CHANNEL,
        f"#START by [{user.first_name}](tg://user?id={user.id}) | `{user.id}`"
    )
