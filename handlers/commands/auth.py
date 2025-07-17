from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL
from database.memory_cache import auth_users  # in-memory live dict

# MongoDB Setup
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.biolink_remover
auth_col = db.auth_users

# ✅ Add authorized user
async def add_auth_user(chat_id: int, user_id: int):
    await auth_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"user_ids": user_id}},
        upsert=True
    )
    await refresh_auth_cache(chat_id)

# ✅ Remove authorized user
async def remove_auth_user(chat_id: int, user_id: int):
    await auth_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"user_ids": user_id}},
    )
    await refresh_auth_cache(chat_id)

# ✅ Get current authorized users from memory (always synced after write)
async def get_auth_users(chat_id: int) -> list:
    if chat_id not in auth_users:
        await refresh_auth_cache(chat_id)
    return auth_users.get(chat_id, [])

# ✅ Load from Mongo and refresh memory
async def refresh_auth_cache(chat_id: int):
    doc = await auth_col.find_one({"chat_id": chat_id}) or {}
    auth_users[chat_id] = doc.get("user_ids", [])
