from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def init(app):
    @app.on_message(filters.command("start"))
    async def start(_, message: Message):
        text = (
            "👋 <b>Welcome to Link Scan Bot!</b>🛡️\n"
            "I protect your groups from:\n"
            "• Unwanted links in bios and messages\n"
            "• Spam users with external URLs\n\n"
            "🔧 <b>Features:</b>\n"
            "• Auto-link removal in chat\n"
            "• Bio link scans\n"
            "• Custom warnings, mute/ban\n"
            "• Whitelist trusted users\n\n"
            "➕ Add me to your group to activate protection.\n"
            "🤖 Powered by <a href='https://t.me/GrayBots'>@GrayBots</a>"
        )

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url="https://t.me/LinkScanBot?startgroup=true")],
            [InlineKeyboardButton("🛠 Updates", url="https://t.me/GrayBots"),
             InlineKeyboardButton("💬 Support", url="https://t.me/GrayBots")]
        ])

        await message.reply(text, reply_markup=buttons)
