# Async MongoDB handler for bioscan toggles
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
bioscan_settings = db["bioscan_settings"]

async def set_bioscan_status(chat_id: int, enabled: bool):
    await bioscan_settings.update_one(
        {"chat_id": chat_id},
        {"$set": {"enabled": enabled}},
        upsert=True
    )

async def get_bioscan_status(chat_id: int) -> bool:
    doc = await bioscan_settings.find_one({"chat_id": chat_id})
    return doc.get("enabled", False) if doc else False
