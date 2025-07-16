# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠 Help", callback_data="help_menu")],
        [InlineKeyboardButton("📣 Updates", url="https://t.me/GrayBots")],
    ])

def commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 /allow", callback_data="help_allow")],
        [InlineKeyboardButton("⚠️ /warn", callback_data="help_warn")],
        [InlineKeyboardButton("🔇 /mute", callback_data="help_mute")],
        [InlineKeyboardButton("⛔ /ban", callback_data="help_ban")],
        [InlineKeyboardButton("🔁 Back", callback_data="main_menu")],
    ])
