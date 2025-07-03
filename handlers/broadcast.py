from pyrogram import filters
from pyrogram.types import Message
from database.mongo import users, chats

@filters.command("broadcast")
def broadcast_handler(client, message: Message):
    if not message.reply_to_message:
        return message.reply("❌ Please reply to a message to broadcast.")

    mode = message.text.split(" ")[-1].strip()
    sent, failed = 0, 0

    if mode == "-all":
        targets = list(users.find()) + list(chats.find())
    elif mode == "-user":
        targets = users.find()
    elif mode == "-group":
        targets = chats.find()
    else:
        return message.reply("❌ Invalid mode. Use `-all`, `-user`, or `-group`.")

    for target in targets:
        _id = target.get("user_id") or target.get("chat_id")
        try:
            client.copy_message(_id, message.chat.id, message.reply_to_message.id)
            sent += 1
        except:
            failed += 1

    message.reply(f"📢 Broadcast complete!\n✅ Sent: {sent}\n❌ Failed: {failed}")
