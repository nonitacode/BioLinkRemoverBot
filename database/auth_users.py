from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["BioLinkRemover"]
auth_col = db["auth_users"]

# In-memory cache
auth_cache = {}

async def refresh_auth_cache(chat_id: int):
    """Refreshes the auth cache for a chat."""
    cursor = auth_col.find({"chat_id": chat_id})
    auth_users = [doc["user_id"] async for doc in cursor]
    auth_cache[chat_id] = set(auth_users)

async def add_auth_user(chat_id: int, user_id: int):
    await auth_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"chat_id": chat_id, "user_id": user_id}},
        upsert=True
    )

async def remove_auth_user(chat_id: int, user_id: int):
    await auth_col.delete_one({"chat_id": chat_id, "user_id": user_id})

async def get_auth_users(chat_id: int):
    if chat_id not in auth_cache:
        await refresh_auth_cache(chat_id)
    return list(auth_cache.get(chat_id, []))

async def is_user_authorized(chat_id: int, user_id: int):
    if chat_id not in auth_cache:
        await refresh_auth_cache(chat_id)
    return user_id in auth_cache.get(chat_id, [])
