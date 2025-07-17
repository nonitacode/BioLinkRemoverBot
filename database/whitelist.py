# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
whitelist_col = db["whitelists"]

async def add_to_whitelist(chat_id: int, user_id: int):
    await whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

async def remove_from_whitelist(chat_id: int, user_id: int):
    await whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"users": user_id}}
    )

async def get_whitelisted_users(chat_id: int) -> list:
    group = await whitelist_col.find_one({"chat_id": chat_id}) or {}
    return group.get("users", [])

async def is_user_whitelisted(chat_id: int, user_id: int) -> bool:
    group = await whitelist_col.find_one({"chat_id": chat_id})
    return user_id in group.get("users", []) if group else False
