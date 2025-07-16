# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.user_language import get_user_language
from utils.language import get_message
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATES_CHANNEL

@Client.on_callback_query(filters.regex("start_panel"))
async def start_panel_cb(client, query: CallbackQuery):
    user = query.from_user
    lang = get_user_language(user.id)
    welcome_text = get_message(lang, "welcome_message").format(user=user.mention)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("📚 Help", callback_data="help_panel"),
            InlineKeyboardButton("👤 Developer", url="https://t.me/StormBreakerz")
        ],
        [
            InlineKeyboardButton("💬 Support Group", url=SUPPORT_GROUP),
            InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)
        ]
    ])
    await query.message.edit_caption(caption=welcome_text, reply_markup=buttons)
