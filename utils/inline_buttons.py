# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATES_CHANNEL

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👤 Developer", url="https://t.me/nikchil"),
            InlineKeyboardButton("📚 Help Menu", callback_data="help_panel")
        ],
        [
            InlineKeyboardButton("💬 Support", url=SUPPORT_GROUP),
            InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)
        ]
    ])
def commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 /allow", callback_data="help_allow")],
        [InlineKeyboardButton("⚠️ /warn", callback_data="help_warn")],
        [InlineKeyboardButton("🔇 /mute", callback_data="help_mute")],
        [InlineKeyboardButton("⛔ /ban", callback_data="help_ban")],
        [InlineKeyboardButton("🔁 Back", callback_data="main_menu")],
    ])
