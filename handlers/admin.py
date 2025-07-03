from pyrogram import Client
from pyrogram.types import Message
from utils.tools import is_admin
from utils.db import get_stats

async def stats_handler(client: Client, message: Message):
    if message.chat.type != "private":
        if not await is_admin(client, message.chat.id, client.me.id):
            await message.reply_text("⚠️ I need to be **admin** to view stats in this group.")
            return

    groups, users = await get_stats()
    await message.reply_text(
        f"📊 **Bot Statistics:**\n\n"
        f"👥 Total Groups: `{groups}`\n"
        f"🙋‍♂️ Total Whitelisted Users: `{users}`"
    )
