# handlers/callbacks/help.py

from bot.bot import app  # ✅ Import the correct Client instance
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.language import get_message
from database.user_language import get_user_language
from config import SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from utils.inline_buttons import commands_buttons  # your help command list

@app.on_callback_query(filters.regex("help_panel"))
async def help_panel_cb(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    help_text = get_message(lang, "help_message")

    await query.message.edit_text(
        text=help_text,
        reply_markup=commands_buttons(),
        disable_web_page_preview=True
    )
