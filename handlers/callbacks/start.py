# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery, InputMediaPhoto
from utils.language import get_message
from database.user_language import get_user_language
from config import START_IMG
from utils.inline_buttons import start_buttons

@app.on_callback_query(filters.regex("main_menu"))
async def main_menu_cb(client, query: CallbackQuery):
    user = query.from_user
    lang = get_user_language(user.id)
    welcome_message = get_message(lang, "welcome_message").format(user=user.mention)

    try:
        await query.message.edit_media(
            media=InputMediaPhoto(media=START_IMG, caption=welcome_message),
            reply_markup=start_buttons()
        )
    except:
        await query.message.edit_text(welcome_message, reply_markup=start_buttons())
