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

async def commands_buttons(user_id: int):
    lang_code = get_user_language(user_id)

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_message(lang_code, "ALLOW"), callback_data="help_allow")],
        [InlineKeyboardButton(get_message(lang_code, "WARN"), callback_data="help_warn")],
        [InlineKeyboardButton(get_message(lang_code, "MUTE"), callback_data="help_mute")],
        [InlineKeyboardButton(get_message(lang_code, "BAN"), callback_data="help_ban")],
        [InlineKeyboardButton(get_message(lang_code, "BACK"), callback_data="main_menu")],
    ])
