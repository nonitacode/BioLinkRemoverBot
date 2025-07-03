from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from config import BOT_NAME

def init(app):
    @app.on_message(filters.command("start"))
    async def start_cmd(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{BOT_NAME}?startgroup=true")],
            [InlineKeyboardButton("🛠 Support", url="https://t.me/GrayBots"), InlineKeyboardButton("🔄 Updates", url="https://t.me/GrayBots")]
        ])

        await message.reply(
            "👋 <b>Welcome to Link Scan Bot!</b>\n\n🛡 I protect your groups from:\n• Unwanted links in bios and messages\n• Spam users with external URLs\n\n🔧 Features:\n• Auto-link removal in chat\n• Bio link scans\n• Custom warnings, mute/ban\n• Whitelist trusted users\n\n➕ Add me to your group to activate protection.\n🤖 Powered by @GrayBots",
            reply_markup=keyboard
        )
