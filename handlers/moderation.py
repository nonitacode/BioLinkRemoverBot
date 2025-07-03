from pyrogram.types import Message, ChatPermissions
from pyrogram import filters
from utils.filters import contains_link
from database.core import is_whitelisted, add_to_whitelist, remove_from_whitelist, increment_violations
from config import MAX_VIOLATIONS

def init(app):
    @app.on_message(filters.command("free"))
    async def free_user(_, message: Message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            add_to_whitelist(user_id)
            await message.reply(f"✅ <code>{user_id}</code> whitelisted.")

    @app.on_message(filters.command("unfree"))
    async def unfree_user(_, message: Message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            remove_from_whitelist(user_id)
            await message.reply(f"❌ <code>{user_id}</code> removed from whitelist.")

    @app.on_message(filters.group & filters.text)
    async def monitor_message(_, message: Message):
        if message.from_user and is_whitelisted(message.from_user.id):
            return

        if contains_link(message.text):
            try:
                await message.delete()
                count = increment_violations(message.from_user.id)
                if count >= MAX_VIOLATIONS:
                    await message.chat.ban_member(message.from_user.id)
                    await message.reply(f"🚫 User banned for {count} violations.")
                elif count == 2:
                    await message.chat.restrict_member(message.from_user.id, ChatPermissions(can_send_messages=False))
                    await message.reply("🔇 User muted due to repeated links.")
                else:
                    await message.reply("⚠️ No links allowed here.")
            except Exception as e:
                print(f"Permission error: {e}")
