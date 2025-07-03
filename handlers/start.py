from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text(
        "**👋 Welcome to LinkScanBot!**\n\n"
        "I'm here to protect your group by scanning messages and bios for suspicious links.\n\n"
        "**Commands:**\n"
        "- `/help` – Show help\n"
        "- `/settings` – Configure bot\n"
        "- `/about` – Bot info and stats\n\n"
        "Add me to your group and make me admin to get started.",
        reply_markup=None  # You can add buttons here if you like
    )
