from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from config import MAX_VIOLATIONS
from database.mongo import is_whitelisted

violations = {}

def _link_checker(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text.lower()

    if is_whitelisted(chat_id, user_id):
        return

    if any(x in text for x in ["http", ".me", "t.me", "@", ".com"]):
        try:
            client.delete_messages(chat_id, message.id)
        except:
            return

        key = f"{chat_id}:{user_id}"
        violations[key] = violations.get(key, 0) + 1

        if violations[key] >= MAX_VIOLATIONS:
            try:
                client.restrict_chat_member(chat_id, user_id, permissions={})
                message.reply(f"🔇 {message.from_user.mention} muted for repeated link posting.")
            except:
                pass

# Export as valid MessageHandler for main.py
link_checker = MessageHandler(_link_checker, filters.group & filters.text)
