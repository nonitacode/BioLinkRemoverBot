from pyrogram import filters
from pyrogram.types import Message
from database.mongo import chats

@filters.command("settings")
def settings_cmd(client, message: Message):
    if "on" in message.text.lower():
        chats.update_one({"chat_id": message.chat.id}, {"$set": {"scan_enabled": True}}, upsert=True)
        message.reply("✅ Link scanning enabled.")
    elif "off" in message.text.lower():
        chats.update_one({"chat_id": message.chat.id}, {"$set": {"scan_enabled": False}}, upsert=True)
        message.reply("❌ Link scanning disabled.")
    else:
        message.reply("Use `/settings on` or `/settings off`.")
