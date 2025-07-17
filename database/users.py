# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]  # Unified naming with your mongo.py
users_collection = db["users"]

async def store_user_data(user_id: int, username: str, full_name: str):
    await users_collection.update_one(
        {"_id": user_id},
        {"$set": {
            "username": username,
            "full_name": full_name
        }},
        upsert=True
    )

async def get_user_language(user_id: int) -> str:
    user = await users_collection.find_one({"_id": user_id})
    return user.get("language", "en") if user else "en"

async def set_user_language(user_id: int, language_code: str):
    await users_collection.update_one(
        {"_id": user_id},
        {"$set": {"language": language_code}},
        upsert=True
    )

async def get_users_count() -> int:
    return await users_collection.count_documents({})
