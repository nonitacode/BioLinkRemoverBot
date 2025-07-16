# handlers/callbacks/start.py

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
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
        # ✅ FIXED: InputMediaPhoto used correctly
        await query.message.edit_media(
            media=InputMediaPhoto(media=START_IMG, caption=welcome_message),
            reply_markup=start_buttons()
        )
    except Exception as e:
        print(f"[start_panel_cb error]: {e}")
        try:
            await query.message.edit_text(welcome_message, reply_markup=start_buttons())
        except Exception as e2:
            print(f"[start_panel_cb fallback error]: {e2}")
