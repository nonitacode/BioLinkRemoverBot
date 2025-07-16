from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME, UPDATE_CHANNEL, SUPPORT_CHAT

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("About Me", callback_data="about_me"),
         InlineKeyboardButton("Donate", callback_data="donate")],
        [InlineKeyboardButton("Commands", callback_data="commands"),
         InlineKeyboardButton("🌐 Language", callback_data="choose_lang")],
        [InlineKeyboardButton("Updates", url=f"https://t.me/{UPDATE_CHANNEL}"),
         InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")],
        [InlineKeyboardButton("Add me in your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])

def commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Bot Commands", callback_data="bot_commands"),
         InlineKeyboardButton("User Commands", callback_data="user_commands")],
        [InlineKeyboardButton("Moderation Commands", callback_data="moderation_commands"),
         InlineKeyboardButton("Admin Commands", callback_data="admin_commands")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main"),
         InlineKeyboardButton("✖️ Close", callback_data="close_menu")]
    ])

def bot_commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("/start", callback_data="start"),
         InlineKeyboardButton("/ping", callback_data="ping")],
        [InlineKeyboardButton("/alive", callback_data="alive"),
         InlineKeyboardButton("/stats", callback_data="stats")],
        [InlineKeyboardButton("⬅️ Back", callback_data="commands"),
         InlineKeyboardButton("✖️ Close", callback_data="close_menu")]
    ])

def user_commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("/addauth", callback_data="addauth"),
         InlineKeyboardButton("/removeauth", callback_data="removeauth")],
        [InlineKeyboardButton("/warn", callback_data="warn"),
         InlineKeyboardButton("/profile", callback_data="profile")],
        [InlineKeyboardButton("⬅️ Back", callback_data="commands"),
         InlineKeyboardButton("✖️ Close", callback_data="close_menu")]
    ])

def moderation_commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("/ban", callback_data="ban"),
         InlineKeyboardButton("/mute", callback_data="mute")],
        [InlineKeyboardButton("/unmute", callback_data="unmute"),
         InlineKeyboardButton("/spam", callback_data="spam")],
        [InlineKeyboardButton("⬅️ Back", callback_data="commands"),
         InlineKeyboardButton("✖️ Close", callback_data="close_menu")]
    ])

def admin_commands_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("/admincache", callback_data="admincache"),
         InlineKeyboardButton("/clearcache", callback_data="clearcache")],
        [InlineKeyboardButton("⬅️ Back", callback_data="commands"),
         InlineKeyboardButton("✖️ Close", callback_data="close_menu")]
    ])

def language_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
         InlineKeyboardButton("🇮🇳 हिन्दी", callback_data="lang_hi")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
         InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es")],
        [InlineKeyboardButton("🇧🇷 Português", callback_data="lang_pt"),
         InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")]
    ])
