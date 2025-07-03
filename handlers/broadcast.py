from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS  # Make sure ADMINS is a list of allowed user IDs
import asyncio

# Broadcast handler for /broadcast command
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast_handler(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("❗ Usage: `/broadcast your message here`", quote=True)
        return

    broadcast_text = message.text.split(None, 1)[1]

    sent_count = 0
    failed_count = 0

    # Get all users from DB if available, else broadcast to groups only (example)
    from LinkScanBot.database import get_all_users  # assume this exists

    users = await get_all_users()

    for user_id in users:
        try:
            await client.send_message(chat_id=user_id, text=broadcast_text)
            sent_count += 1
            await asyncio.sleep(0.1)  # avoid hitting flood limit
        except Exception:
            failed_count += 1
            continue

    await message.reply_text(
        f"📢 Broadcast completed!\n\n✅ Sent: {sent_count}\n❌ Failed: {failed_count}"
    )
