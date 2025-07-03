from pymongo import MongoClient
from config import MONGO_URL, MAX_VIOLATIONS, LOG_CHANNEL
from pyrogram.enums import ChatPermissions

client = MongoClient(MONGO_URL)
db = client.linkscan
whitelist = db.whitelist
violations = db.violations
group_settings = db.settings
users = db.users
chats = db.chats

def is_whitelisted(user_id: int, chat_id: int) -> bool:
    return whitelist.find_one({"user_id": user_id, "chat_id": chat_id}) is not None

def whitelist_user(user_id: int, chat_id: int):
    whitelist.update_one({"user_id": user_id, "chat_id": chat_id}, {"$set": {"user_id": user_id}}, upsert=True)

def remove_whitelist(user_id: int, chat_id: int):
    whitelist.delete_one({"user_id": user_id, "chat_id": chat_id})

def get_group_settings(chat_id: int):
    return group_settings.find_one({"chat_id": chat_id}) or {"enabled": True}

def set_group_setting(chat_id: int, key: str, value):
    group_settings.update_one({"chat_id": chat_id}, {"$set": {key: value}}, upsert=True)

def record_violation(bot, chat_id: int, user_id: int, message):
    user_data = violations.find_one({"chat_id": chat_id, "user_id": user_id}) or {"count": 0}
    new_count = user_data["count"] + 1
    violations.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"count": new_count}}, upsert=True)

    if LOG_CHANNEL:
        try:
            bot.send_message(LOG_CHANNEL, f"🚨 Violation in {chat_id} by [{user_id}](tg://user?id={user_id}): {message.text or 'media'}")
        except:
            pass

    if new_count >= MAX_VIOLATIONS:
        try:
            bot.restrict_chat_member(chat_id, user_id, ChatPermissions())
            bot.send_message(chat_id, f"🔇 User [ID:{user_id}] auto-muted for repeated violations.")
        except Exception as e:
            print(f"Failed to restrict user {user_id}: {e}")

def take_action(bot, chat_id: int, user_id: int):
    record_violation(bot, chat_id, user_id, message=None)

def get_target_ids(mode: str):
    group_ids = [c["chat_id"] for c in chats.find()] if mode in ["all", "group"] else []
    user_ids = [u["user_id"] for u in users.find()] if mode in ["all", "user"] else []
    return list(set(group_ids + user_ids))
