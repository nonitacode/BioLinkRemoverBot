# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.user_language import get_user_language
from utils.language import get_message
from config import BOT_USERNAME, SUPPORT_GROUP

@Client.on_callback_query(filters.regex("help_panel"))
async def help_panel_cb(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    help_text = get_message(lang, "help_message")

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👤 Developer", url="https://t.me/StormBreakerz"),
            InlineKeyboardButton("💬 Support", url=SUPPORT_GROUP)
        ],
        [InlineKeyboardButton("⬅️ Back to Start", callback_data="start_panel")]
    ])
    await query.message.edit_caption(caption=help_text, reply_markup=buttons)
