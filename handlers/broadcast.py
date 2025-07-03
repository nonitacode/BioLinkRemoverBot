from pyrogram.errors import FloodWait
import asyncio

@filters.command("broadcast") & filters.user(lambda _, __, m: m.from_user and m.from_user.is_chat_admin)
def broadcast_handler(client, message: Message):
    if not message.reply_to_message:
        return message.reply("Reply to a message with `/broadcast -all`, `-group`, or `-user`", quote=True)

    args = message.text.split()
    if len(args) != 2 or args[1] not in ["-all", "-group", "-user"]:
        return message.reply("Usage: /broadcast -all | -group | -user", quote=True)

    mode = args[1][1:]  # 'all', 'group', or 'user'
    target_ids = get_target_ids(mode)

    original = message.reply_to_message
    sent, failed = 0, 0
    message.reply(f"📢 Starting `{mode}` broadcast to {len(target_ids)} targets...")

    for target_id in target_ids:
        try:
            original.copy(target_id)
            sent += 1
        except FloodWait as e:
            asyncio.sleep(e.value)
        except:
            failed += 1

    message.reply(f"✅ Broadcast finished.\n✅ Sent: {sent}\n❌ Failed: {failed}")


# database/mongo.py additions

users = db.users
chats = db.chats

# Update to collect IDs by type
def get_target_ids(mode: str):
    group_ids = [c["chat_id"] for c in chats.find()] if mode in ["all", "group"] else []
    user_ids = [u["user_id"] for u in users.find()] if mode in ["all", "user"] else []
    return list(set(group_ids + user_ids))


# Add to message_scan or main to store user/group IDs:
# Store group/user for broadcast
@app.on_message(filters.all)
def track_entities(client, message):
    if message.chat.type in ["group", "supergroup"]:
        chats.update_one({"chat_id": message.chat.id}, {"$set": {"chat_id": message.chat.id}}, upsert=True)
    elif message.chat.type == "private":
        users.update_one({"user_id": message.from_user.id}, {"$set": {"user_id": message.from_user.id}}, upsert=True)
