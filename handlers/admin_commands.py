from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from database.mongo import add_whitelist, remove_whitelist

# Define command logic
def whitelist_cmd(client, message: Message):
    if not message.reply_to_message:
        return message.reply("❗ Reply to a user to whitelist.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    add_whitelist(chat_id, user_id)
    message.reply(f"✅ Whitelisted {message.reply_to_message.from_user.mention}")

def unwhitelist_cmd(client, message: Message):
    if not message.reply_to_message:
        return message.reply("❗ Reply to a user to unwhitelist.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    remove_whitelist(chat_id, user_id)
    message.reply(f"🚫 Removed {message.reply_to_message.from_user.mention} from whitelist.")

# Export proper handler objects
admin_cmds = [
    MessageHandler(whitelist_cmd, filters.command("whitelist") & filters.group),
    MessageHandler(unwhitelist_cmd, filters.command("unwhitelist") & filters.group)
]
