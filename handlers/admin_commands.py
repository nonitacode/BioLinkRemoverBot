from pyrogram import filters
from pyrogram.types import Message
from database.mongo import whitelist_user, remove_whitelist

@filters.command("whitelist")
def whitelist_cmd(client, message: Message):
    if not message.reply_to_message:
        return message.reply("❌ Reply to a user to whitelist.")
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    whitelist_user(chat_id, user_id)
    message.reply("✅ User whitelisted.")

@filters.command("unwhitelist")
def unwhitelist_cmd(client, message: Message):
    if not message.reply_to_message:
        return message.reply("❌ Reply to a user to unwhitelist.")
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    remove_whitelist(chat_id, user_id)
    message.reply("✅ User removed from whitelist.")
