# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATES_CHANNEL
from utils.language import get_message  # Adjust path if needed

async def start_buttons(user_id: int):
    lang_code = get_user_language(user_id)

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_message(lang_code, "ADD_BUTTON"), url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton(get_message(lang_code, "DEVELOPER_BUTTON"), url="https://t.me/nikchil"),
            InlineKeyboardButton(get_message(lang_code, "HELP_MENU_BUTTON"), callback_data="help_panel")
        ],
        [
            InlineKeyboardButton(get_message(lang_code, "SUPPORT_BUTTON"), url=SUPPORT_GROUP),
            InlineKeyboardButton(get_message(lang_code, "UPDATES_BUTTON"), url=UPDATES_CHANNEL)
        ],
        [InlineKeyboardButton(get_message(lang_code, "LANGUAGE_BUTTON"), callback_data="language_panel")]
    ])
    ])

async def commands_buttons(chat_id: int):
    lang = get_message("en", "buttons")

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(lang["ALLOW"], callback_data="help_allow")],
        [InlineKeyboardButton(lang["WARN"], callback_data="help_warn")],
        [InlineKeyboardButton(lang["MUTE"], callback_data="help_mute")],
        [InlineKeyboardButton(lang["BAN"], callback_data="help_ban")],
        [InlineKeyboardButton(lang["BACK"], callback_data="main_menu")],
    ])
