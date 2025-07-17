from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL
from cachetools import TTLCache

# MongoDB Setup
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.biolink_remover

# Memory cache for authorized users (cache per group, expires after 1 hour)
auth_cache = TTLCache(maxsize=10000, ttl=3600)

# Collection
auth_col = db.auth_users


# ✅ Add an authorized user
async def add_auth_user(chat_id: int, user_id: int):
    await auth_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"user_ids": user_id}},
        upsert=True
    )
    await refresh_auth_cache(chat_id)


# ✅ Remove an authorized user
async def remove_auth_user(chat_id: int, user_id: int):
    await auth_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"user_ids": user_id}},
    )
    await refresh_auth_cache(chat_id)


# ✅ Get all authorized users
async def get_auth_users(chat_id: int) -> list:
    if chat_id in auth_cache:
        return auth_cache[chat_id]

    doc = await auth_col.find_one({"chat_id": chat_id}) or {}
    users = doc.get("user_ids", [])
    auth_cache[chat_id] = users
    return users


# ✅ Refresh in-memory cache
async def refresh_auth_cache(chat_id: int):
    doc = await auth_col.find_one({"chat_id": chat_id}) or {}
    auth_cache[chat_id] = doc.get("user_ids", [])
