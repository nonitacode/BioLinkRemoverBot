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
                InlineKeyboardButton("Developer", url=DEVELOPER),
                InlineKeyboardButton("Help Menu", callback_data="show_help")
            ],
            [
                InlineKeyboardButton("Support", url=SUPPORT_GROUP),
                InlineKeyboardButton("Updates", url=UPDATES_CHANNEL)
            ]
        ])

        await message.reply(
            f"""
👋 <b>Welcome to <u>Bio Link Remover Bot</u>!</b>

🛡️ <b>Cleaner Groups, Safer Chats</b>
• Detects links in bios/usernames
• Auto-warns, mutes, or bans violators
• Prevents spam and phishing

🧰 <b>Features:</b>
• Real-time moderation
• Whitelisting system
• Broadcast to users/groups
• Easy admin tools & memory caching

<i>Use the buttons below to get started 👇</i>
            """,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
