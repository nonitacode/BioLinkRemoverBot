from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
warn_col = db["user_warns"]

async def warn_user(chat_id: int, user_id: int) -> int:
    data = await warn_col.find_one({"chat_id": chat_id, "user_id": user_id})
    count = (data.get("warns", 0) + 1) if data else 1
    await warn_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"warns": count}},
        upsert=True
    )
    return count

async def get_warnings(chat_id: int, user_id: int) -> int:
    data = await warn_col.find_one({"chat_id": chat_id, "user_id": user_id})
    return data.get("warns", 0) if data else 0

async def reset_warnings(chat_id: int, user_id: int):
    await warn_col.delete_one({"chat_id": chat_id, "user_id": user_id})
