from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

BOT_USERNAME = "BioLinkRemoverBot"
SUPPORT_GROUP = "https://t.me/GrayBotSupport"
UPDATES_CHANNEL = "https://t.me/GrayBots"
DEVELOPER = "https://t.me/Nikchil"

def init(app):
    @app.on_message(filters.command("start"))
    async def start(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("🛠 Help", callback_data="show_help"),
                InlineKeyboardButton("👨‍💻 Developer", url=DEVELOPER)
            ],
            [
                InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL),
                InlineKeyboardButton("🆘 Support", url=SUPPORT_GROUP)
            ]
        ])

        await message.reply(
            f"""
👋 <b>Welcome to Bio Link Remover Bot!</b> 🛡️

<b>I protect your groups from:</b>  
• Unwanted links in bios and messages  
• Spam users with external URLs

<b>🔧 Features:</b>  
• Auto-link removal in chat  
• Bio link scans  
• Custom warnings, mute/ban  
• Whitelist trusted users

➕ <b>Add me to your group to activate protection.</b>  
🤖 <i>Powered by</i> <a href="{UPDATES_CHANNEL}">@GrayBots</a>
            """,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
