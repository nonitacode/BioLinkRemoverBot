from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
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
    "whitelist": set(),
    "configs": {},
}

async def refresh_memory_cache():
    whitelist = await get_all_whitelist()
    memory_cache["whitelist"] = set(whitelist)
    memory_cache["configs"] = {
        doc["_id"]: {
            "warn_limit": doc.get("warn_limit", 3),
            "punishment_mode": doc.get("punishment_mode", "mute"),
            "bio_scan": doc.get("bio_scan", False)
        }
        async for doc in config_col.find()
    }
    return True

async def get_memory_config(chat_id):
    return memory_cache["configs"].get(chat_id, {
        "warn_limit": 3,
        "punishment_mode": "mute",
        "bio_scan": False
    })

async def set_bio_scan(chat_id, enabled: bool):
    await config_col.update_one(
        {"_id": chat_id},
        {"$set": {"_id": chat_id, "bio_scan": enabled}},
        upsert=True
    )
    await refresh_memory_cache()
    memory_cache["configs"].setdefault(chat_id, {})["bio_scan"] = enabled

async def is_whitelisted(user_id):
    return user_id in memory_cache["whitelist"]

async def add_to_whitelist(user_id):
    await whitelist_col.update_one(
        {"_id": user_id},
        {"$set": {"_id": user_id}},
        upsert=True
    )
    await refresh_memory_cache()

async def remove_from_whitelist(user_id):
    await whitelist_col.delete_one({"_id": user_id})
    await refresh_memory_cache()

async def get_all_whitelist():
    return [doc["_id"] async for doc in whitelist_col.find()]

async def increment_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    result = await violations_col.find_one_and_update(
        {"_id": key}, 
        {"$inc": {"count": 1}}, 
        upsert=True, 
        return_document=True
    )
    return result["count"]

async def get_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = await violations_col.find_one({"_id": key})
    return doc["count"] if doc else 0

async def remove_user_record(user_id):
    await violations_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    await warn_cache_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    await backup_col.delete_many({"_id": {"$regex": f":{user_id}$"}})

async def set_last_warn(chat_id, user_id, message_id):
    key = f"{chat_id}:{user_id}"
    await warn_cache_col.update_one(
        {"_id": key},
        {"$set": {"_id": key, "message_id": message_id}},
        upsert=True
    )

async def get_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return await warn_cache_col.find_one({"_id": key})

async def delete_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    await warn_cache_col.delete_one({"_id": key})

async def save_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = await violations_col.find_one({"_id": key})
    if doc:
        await backup_col.update_one({"_id": key}, {"$set": doc}, upsert=True)

async def restore_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = await backup_col.find_one({"_id": key})
    if doc:
        await violations_col.replace_one({"_id": key}, doc, upsert=True)
        await backup_col.delete_one({"_id": key})

async def get_served_users():
    return [doc["user_id"] async for doc in users_col.find({}, {"_id": 0, "user_id": 1})]

async def get_served_chats():
    return [doc["chat_id"] async for doc in groups_col.find({}, {"_id": 0, "chat_id": 1})]

async def add_served_user(user_id):
    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def add_served_chat(chat_id):
    await groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id}},
        upsert=True
    )
