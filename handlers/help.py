from pyrogram import Client
from pyrogram.types import Message

async def help_handler(client: Client, message: Message):
    await message.reply_text(
        "**📚 Help - LinkScanBot**\n\n"
        "🛡 **Auto Monitoring:**\n"
        "• Scans all messages & bios for malicious links\n"
        "• Deletes, bans or mutes users automatically\n\n"
        "👑 **Admin Tools:**\n"
        "• /stats or /about – Check bot's group stats\n\n"
        "✅ **Whitelisting:**\n"
        "• Bot respects whitelisted users/groups\n\n"
        "📁 **Inline Buttons:**\n"
        "• Help menus with step-by-step guidance\n\n"
        "For questions, contact bot owner."
    )
