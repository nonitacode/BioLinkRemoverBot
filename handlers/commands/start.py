# handlers/callbacks/start.py

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.language import get_message
from database.user_language import get_user_language
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATES_CHANNEL, START_IMG
from utils.inline_buttons import start_buttons

@app.on_callback_query(filters.regex("start_panel"))
async def start_panel_cb(client, query: CallbackQuery):
    user = query.from_user
    lang = get_user_language(user.id)
    welcome_message = get_message(lang, "welcome_message").format(user=user.mention)

    try:
        # ✅ Update the photo + caption using edit_media
        await query.message.edit_media(
            media={"type": "photo", "media": START_IMG, "caption": welcome_message},
            reply_markup=start_buttons()
        )
    except:
        # Fallback for plain text messages
        await query.message.edit_text(welcome_message, reply_markup=start_buttons())
