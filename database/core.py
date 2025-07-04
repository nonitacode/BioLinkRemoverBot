from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.link_scan

# Collections
whitelist_col = db.whitelist
violations_col = db.violations
config_col = db.config
warn_cache_col = db.warn_cache
backup_col = db.violation_backup
users_col = db.served_users
groups_col = db.served_chats

# Memory cache
memory_cache = {
    "whitelist": {},  # per-group whitelist
    "configs": {},
}

def refresh_memory_cache():
    memory_cache["whitelist"] = {}
    for doc in whitelist_col.find():
        try:
            chat_id, user_id = map(int, doc["_id"].split(":"))
            memory_cache["whitelist"].setdefault(chat_id, set()).add(user_id)
        except:
            continue
    memory_cache["configs"] = {
        doc["_id"]: {
            "warn_limit": doc.get("warn_limit", 3),
            "punishment_mode": doc.get("punishment_mode", "mute"),
            "bio_scan": doc.get("bio_scan", False)
        }
        for doc in config_col.find()
    }
    return True

def get_memory_config(chat_id):
    return memory_cache["configs"].get(chat_id, {
        "warn_limit": 3,
        "punishment_mode": "mute",
        "bio_scan": False
    })

def set_bio_scan(chat_id, enabled: bool):
    config_col.update_one(
        {"_id": chat_id},
        {"$set": {"_id": chat_id, "bio_scan": enabled}},
        upsert=True
    )
    refresh_memory_cache()
    memory_cache["configs"].setdefault(chat_id, {})["bio_scan"] = enabled

def get_bio_scan(chat_id):
    return memory_cache["configs"].get(chat_id, {}).get("bio_scan", False)

def is_whitelisted(chat_id, user_id):
    return user_id in memory_cache["whitelist"].get(chat_id, set())

def add_to_whitelist(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    whitelist_col.update_one({"_id": key}, {"$set": {"_id": key}}, upsert=True)
    refresh_memory_cache()

def remove_from_whitelist(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    whitelist_col.delete_one({"_id": key})
    refresh_memory_cache()

def get_group_whitelist(chat_id):
    return list(memory_cache["whitelist"].get(chat_id, []))

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
    # Clears all user violations across all chats
    violations_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    warn_cache_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    backup_col.delete_many({"_id": {"$regex": f":{user_id}$"}})

def set_last_warn(chat_id, user_id, message_id):
    key = f"{chat_id}:{user_id}"
    warn_cache_col.update_one(
        {"_id": key},
        {"$set": {"_id": key, "message_id": message_id}},
        upsert=True
    )

def get_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return warn_cache_col.find_one({"_id": key})

def delete_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    warn_cache_col.delete_one({"_id": key})

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

async def get_served_users():
    return list(users_col.find({}, {"_id": 0, "user_id": 1}))

async def get_served_chats():
    return list(groups_col.find({}, {"_id": 0, "chat_id": 1}))

async def add_served_user(user_id):
    users_col.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

async def add_served_chat(chat_id):
    groups_col.update_one({"chat_id": chat_id}, {"$set": {"chat_id": chat_id}}, upsert=True)
