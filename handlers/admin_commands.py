from pyrogram import filters
from pyrogram.types import Message
from database.mongo import whitelist_user, remove_whitelist

@filters.command(["whitelist", "unwhitelist"]) & filters.user(lambda _, __, m: m.from_user and m.from_user.is_chat_admin)
def admin_cmds(client, message: Message):
    cmd = message.command[0].lower()
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        if cmd == "whitelist":
            whitelist_user(user_id, chat_id)
            message.reply("✅ User whitelisted.")
        elif cmd == "unwhitelist":
            remove_whitelist(user_id, chat_id)
            message.reply("🗑 User removed from whitelist.")
