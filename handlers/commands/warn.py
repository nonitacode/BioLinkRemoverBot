from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.warn_db import warn_user, get_warnings
from utils.language import get_message

@app.on_message(filters.command("warn") & filters.group)
async def warn_command(client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply("⚠️ Reply to a user or provide user ID or mention.")

    user = message.reply_to_message.from_user if message.reply_to_message else await client.get_users(message.command[1])
    count = await warn_user(message.chat.id, user.id)
    await message.reply(f"⚠️ {user.mention} has been warned.\nTotal Warnings: {count}")
