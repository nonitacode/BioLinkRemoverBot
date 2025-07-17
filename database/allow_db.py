from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
allow_col = db["allowed_users"]

async def allow_user(chat_id: int, user_id: int):
    await allow_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"approved": True}},
        upsert=True
    )

async def is_allowed(chat_id: int, user_id: int) -> bool:
    data = await allow_col.find_one({"chat_id": chat_id, "user_id": user_id})
    return bool(data and data.get("approved", False))
