# modules/inline.py

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME, SUPPORT_CHAT, UPDATE_CHANNEL

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ℹ️ About", callback_data="about_me"),
         InlineKeyboardButton("💖 Donate", callback_data="donate")],
        [InlineKeyboardButton("📚 Commands", callback_data="commands"),
         InlineKeyboardButton("🌐 Language", callback_data="choose_lang")],
        [InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATE_CHANNEL}"),
         InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_CHAT}")],
        [InlineKeyboardButton("➕ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])

def commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 Bot", callback_data="bot_commands"),
         InlineKeyboardButton("👤 User", callback_data="user_commands")],
        [InlineKeyboardButton("🛡️ Moderation", callback_data="moderation_commands"),
         InlineKeyboardButton("⚙️ Admin", callback_data="admin_commands")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main"),
         InlineKeyboardButton("❌ Close", callback_data="close_menu")]
    ])
