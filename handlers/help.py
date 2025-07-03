from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from config import BOT_NAME

def init(app):
    @app.on_message(filters.command("help"))
    async def help_cmd(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{BOT_NAME}?startgroup=true")],
            [InlineKeyboardButton("🛠 Support", url="https://t.me/GrayBots")]
        ])

        await message.reply(
            "<b>🛠️ Bot Commands & Usage</b>\n\n"
            "/config – Set warn-limit & punishment mode\n"
            "/free – Whitelist a user (reply or ID)\n"
            "/unfree – Remove from whitelist\n"
            "/freelist – List all whitelisted users\n\n"
            "<b>Detection Behavior:</b>\n"
            "When someone with a URL or @username in their bio sends a message, the bot will:\n"
            "1. ⚠️ Warn them\n2. 🔇 Mute them after limits\n3. 🔨 Ban (if enabled)\n\n"
            "Admins can use inline buttons to whitelist or unmute.",
            reply_markup=keyboard
        )
