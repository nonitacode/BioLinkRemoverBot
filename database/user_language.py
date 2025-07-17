# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
user_language_col = db["user_languages"]

async def get_user_language(user_id: int) -> str:
    user = await user_language_col.find_one({"_id": user_id})
    if user and "language" in user:
        return user["language"]
    return "en"  # default to English

async def set_user_language(user_id: int, lang_code: str):
    await user_language_col.update_one(
        {"_id": user_id},
        {"$set": {"language": lang_code}},
        upsert=True
    )
