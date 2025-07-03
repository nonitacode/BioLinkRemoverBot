from pyrogram import filters
from pyrogram.types import Message
from filters.link_detector import is_link_message
from database.mongo import is_whitelisted, record_violation, get_group_settings

@filters.group & filters.text
def link_checker(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    settings = get_group_settings(chat_id)

    if not settings.get("enabled", True):
        return

    if is_link_message(message):
        if not is_whitelisted(user_id, chat_id):
            message.delete()
            message.reply_text("🚫 Link or username detected and removed.", quote=False)
            record_violation(client, chat_id, user_id, message)
