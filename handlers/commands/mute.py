from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
from bot.bot import app

@app.on_message(filters.command("mute") & filters.group)
async def mute_command(client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply("⚠️ Reply to a user or provide user ID or mention.")

    user = message.reply_to_message.from_user if message.reply_to_message else await client.get_users(message.command[1])
    try:
        await client.restrict_chat_member(
            message.chat.id,
            user.id,
            ChatPermissions()
        )
        await message.reply(f"🔇 {user.mention} has been muted.")
    except:
        await message.reply("❌ Failed to mute user. Do I have admin rights?")
