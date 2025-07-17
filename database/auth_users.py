# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
auth_users_col = db["auth_users"]

async def add_auth_user(user_id: int):
    await auth_users_col.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def remove_auth_user(user_id: int):
    await auth_users_col.delete_one({"user_id": user_id})

async def get_auth_users() -> list:
    cursor = auth_users_col.find({}, {"_id": 0, "user_id": 1})
    return [doc["user_id"] async for doc in cursor]

async def is_auth_user(user_id: int) -> bool:
    count = await auth_users_col.count_documents({"user_id": user_id})
    return count > 0
