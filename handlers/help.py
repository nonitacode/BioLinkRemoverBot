from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def init(app):
    @app.on_message(filters.command("help"))
    async def help_cmd(_, message: Message):
        text = (
            "🛠️ <b>Bot Commands & Usage</b>\n"
            "/config – Set warn-limit & punishment mode\n"
            "/free – Whitelist a user (reply or user/id)\n"
            "/unfree – Remove from whitelist\n"
            "/freelist – List all whitelisted users\n\n"
            "<b>When someone with a URL in their bio posts, I’ll:</b>\n"
            "1. ⚠️ Warn them\n"
            "2. 🔇 Mute if they exceed limit\n"
            "3. 🔨 Ban if set to ban\n\n"
            "Use the inline buttons on warnings to cancel or whitelist."
        )

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url="https://t.me/BioLinkRemoverBot?startgroup=true")]
        ])

        await message.reply(text, reply_markup=buttons)
