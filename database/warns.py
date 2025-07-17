# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
warns_col = db["warns"]

async def add_warn(user_id: int, chat_id: int, reason: str = "Violation"):
    await warns_col.insert_one({
        "user_id": user_id,
        "chat_id": chat_id,
        "reason": reason
    })

async def get_warns_count(user_id: int, chat_id: int) -> int:
    return await warns_col.count_documents({
        "user_id": user_id,
        "chat_id": chat_id
    })

async def reset_warns(user_id: int, chat_id: int):
    await warns_col.delete_many({
        "user_id": user_id,
        "chat_id": chat_id
    })

async def get_all_warns(chat_id: int) -> list:
    cursor = warns_col.find({"chat_id": chat_id})
    return [doc async for doc in cursor]
