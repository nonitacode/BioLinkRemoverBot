from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("about"))
async def about_handler(client: Client, message: Message):
    text = """
**🤖 About LinkScanBot**

🔍 This bot scans messages and bios in real-time for malicious or suspicious links.

📊 **Bot Features:**
- Auto link scanning
- Join checks for new users
- Admin-only configuration
- Broadcast support
- Full logging

👤 Developed by: [Your Name or Team]
📎 Source Code: [GitHub or Repo Link]
"""
    await message.reply_text(text, quote=True)
