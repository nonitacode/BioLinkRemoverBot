from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app

@app.on_message(filters.command("ban") & filters.group)
async def ban_command(client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply("⚠️ Reply to a user or provide user ID or mention.")

    user = message.reply_to_message.from_user if message.reply_to_message else await client.get_users(message.command[1])
    try:
        await client.ban_chat_member(message.chat.id, user.id)
        await message.reply(f"🔨 {user.mention} has been permanently banned.")
    except:
        await message.reply("❌ Failed to ban user. Do I have admin rights?")
