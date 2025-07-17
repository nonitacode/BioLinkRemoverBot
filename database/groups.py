# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
groups_col = db["groups"]

async def store_group_data(chat_id: int, title: str):
    await groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"title": title}},
        upsert=True
    )

async def get_groups_count() -> int:
    return await groups_col.count_documents({})
