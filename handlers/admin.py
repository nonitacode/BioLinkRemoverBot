from pyrogram.types import Message
from pyrogram import filters
from utils.sudo import is_sudo
from database.core import get_all_whitelist

def init(app):
    @app.on_message(filters.command("ping"))
    async def ping(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 You are not authorized.")
        await message.reply("🏓 Pong!")

    @app.on_message(filters.command("freelist"))
    async def freelist(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Only the bot owner can use this.")
        wl = get_all_whitelist()
        text = "\n".join([f"• <code>{uid}</code>" for uid in wl]) or "⚠️ No whitelisted users."
        await message.reply(text)

    @app.on_message(filters.command("broadcast"))
    async def broadcast(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Not allowed.")

        if not message.reply_to_message:
            return await message.reply("📢 Reply to a message to broadcast it.")

        sent, failed = 0, 0
        # Replace this list with chat_id list from DB
        for chat_id in [message.chat.id]:  # Simulated
            try:
                await app.copy_message(chat_id, message.chat.id, message.reply_to_message.message_id)
                sent += 1
            except:
                failed += 1

        await message.reply(f"✅ Broadcast done. Sent: {sent}, Failed: {failed}")
