from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]
scan_col = db["bioscan"]

async def set_bio_scan(chat_id: int, status: bool):
    await scan_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"enabled": status}},
        upsert=True
    )

async def get_bio_scan(chat_id: int) -> bool:
    data = await scan_col.find_one({"chat_id": chat_id})
    return data.get("enabled", True) if data else True
