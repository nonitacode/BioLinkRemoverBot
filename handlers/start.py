from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, BOT_NAME

BOT_USERNAME = "BioLinkRemoverBot"  # Update if different
SUPPORT_GROUP = "https://t.me/GrayBotSupport"
UPDATES_CHANNEL = "https://t.me/GrayBots"

def init(app):
    @app.on_message(filters.command("start"))
    async def start(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)],
            [InlineKeyboardButton("🆘 Support", url=SUPPORT_GROUP)]
        ])

        await message.reply(
            """
👋 <b>Welcome to Link Scan Bot!</b> 🛡️

<b>I protect your groups from:</b>
• Unwanted links in bios and messages
• Spam users with external URLs

<b>🔧 Features:</b>
• Auto-link removal in chat
• Bio link scans
• Custom warnings, mute/ban
• Whitelist trusted users

➕ <b>Add me to your group to activate protection.</b>
🤖 <i>Powered by</i> <a href="https://t.me/GrayBots">@GrayBots</a>
            """,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    @app.on_message(filters.command("help"))
    async def help(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)],
            [InlineKeyboardButton("🆘 Support", url=SUPPORT_GROUP)]
        ])

        await message.reply(
            """
<b>🛠️ Bot Commands & Usage</b>

/config – Set warn-limit & punishment mode
/free – Whitelist a user (reply or user ID)
/unfree – Remove from whitelist
/freelist – List all whitelisted users

<b>⚙️ How it works:</b>
1. Warns users with suspicious usernames or bio links
2. Mutes/Bans if they exceed violation limit
3. Inline buttons let admins unmute or whitelist

🤖 <i>Powered by</i> <a href="https://t.me/GrayBots">@GrayBots</a>
            """,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
