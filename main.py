from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import message_scan, join_scan, admin_commands, settings, broadcast
from database.mongo import users, chats

app = Client("LinkScanBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers
app.add_handler(message_scan.link_checker)
app.add_handler(join_scan.bio_checker)
app.add_handler(admin_commands.admin_cmds)
app.add_handler(settings.settings_cmd)
app.add_handler(broadcast.broadcast_handler)

# Auto track chats/users
@app.on_message(filters.all)
def track_entities(client, message):
    if message.chat.type in ["group", "supergroup"]:
        chats.update_one({"chat_id": message.chat.id}, {"$set": {"chat_id": message.chat.id}}, upsert=True)
    elif message.chat.type == "private":
        users.update_one({"user_id": message.from_user.id}, {"$set": {"user_id": message.from_user.id}}, upsert=True)

if __name__ == "__main__":
    print("🤖 LinkScanBot Started!")
    app.run()
