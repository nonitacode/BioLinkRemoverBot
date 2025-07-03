from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.link_scan

# MongoDB Collections
whitelist_col = db.whitelist
violations_col = db.violations
config_col = db.config
warn_cache_col = db.warn_cache
backup_col = db.violation_backup
users_col = db.served_users
groups_col = db.served_chats

# Memory cache dictionary
memory_cache = {
    "whitelist": set(),
    "configs": {},
}

# Refresh cache (for /refresh or /admincache)
def refresh_memory_cache():
    memory_cache["whitelist"] = set(get_all_whitelist())
    memory_cache["configs"] = {
        doc["_id"]: {
            "warn_limit": doc.get("warn_limit", 3),
            "punishment_mode": doc.get("punishment_mode", "mute")
        }
        for doc in config_col.find()
    }
    return True

def get_memory_config(chat_id):
    return memory_cache["configs"].get(chat_id, {"warn_limit": 3, "punishment_mode": "mute"})

# Whitelist functions
def is_whitelisted(user_id):
    return user_id in memory_cache["whitelist"]

def add_to_whitelist(user_id):
    whitelist_col.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)
    memory_cache["whitelist"].add(user_id)

def remove_from_whitelist(user_id):
    whitelist_col.delete_one({"_id": user_id})
    memory_cache["whitelist"].discard(user_id)

def get_all_whitelist():
    return [doc["_id"] for doc in whitelist_col.find()]

# Violation tracking
def increment_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return violations_col.find_one_and_update(
        {"_id": key}, {"$inc": {"count": 1}}, upsert=True, return_document=True
    )["count"]

def get_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = violations_col.find_one({"_id": key})
    return doc["count"] if doc else 0

def remove_user_record(user_id):
    violations_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    warn_cache_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    backup_col.delete_many({"_id": {"$regex": f":{user_id}$"}})

# Warning cache
def delete_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    warn_cache_col.delete_one({"_id": key})

def get_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return warn_cache_col.find_one({"_id": key})

def set_last_warn(chat_id, user_id, message_id):
    key = f"{chat_id}:{user_id}"
    warn_cache_col.update_one(
        {"_id": key},
        {"$set": {"_id": key, "message_id": message_id}},
        upsert=True
    )

# Backup/Restore violations
def save_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = violations_col.find_one({"_id": key})
    if doc:
        backup_col.update_one({"_id": key}, {"$set": doc}, upsert=True)

def restore_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = backup_col.find_one({"_id": key})
    if doc:
        violations_col.replace_one({"_id": key}, doc, upsert=True)
        backup_col.delete_one({"_id": key})

# Broadcast utilities
async def get_served_users():
    return list(users_col.find({}, {"_id": 0, "user_id": 1}))

async def get_served_chats():
    return list(groups_col.find({}, {"_id": 0, "chat_id": 1}))

async def add_served_user(user_id):
    users_col.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

async def add_served_chat(chat_id):
    groups_col.update_one({"chat_id": chat_id}, {"$set": {"chat_id": chat_id}}, upsert=True)
