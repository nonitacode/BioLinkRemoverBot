from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    text = """
**🛡️ LinkScanBot Help Guide**

📌 Commands:
- `/help` — Show this help message
- `/settings` — Configure bot settings
- `/about` — About the bot and stats
- `/broadcast [text]` — Send message to all users (admin only)

🧠 How to use:
- Just add this bot to your group.
- It will auto-scan all messages and bios for suspicious links.
- Configure with `/settings` if you're admin.

Need more help? Contact: @YourSupportUsername
"""
    await message.reply_text(text, quote=True)
