# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATES_CHANNEL
from utils.language import get_message  # Adjust path if needed

async def start_buttons(chat_id: int):
    lang = get_message("en", "buttons")  # Hardcoded 'en' for now; make dynamic if needed

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(lang["ADD"], url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton(lang["DEVELOPER"], url="https://t.me/nikchil"),
            InlineKeyboardButton(lang["HELP_MENU"], callback_data="help_panel")
        ],
        [
            InlineKeyboardButton(lang["SUPPORT"], url=SUPPORT_GROUP),
            InlineKeyboardButton(lang["UPDATES"], url=UPDATES_CHANNEL)
        ],
        [InlineKeyboardButton(lang["LANGUAGE"], callback_data="language_panel")]
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
