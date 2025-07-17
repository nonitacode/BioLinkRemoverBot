from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client.biolinkbot
users_collection = db.users

async def store_user_data(user_id, username, full_name):
    await users_collection.update_one(
        {"_id": user_id},
        {"$set": {
            "username": username,
            "full_name": full_name
        }},
        upsert=True
    )

async def get_user_language(user_id):
    user = await users_collection.find_one({"_id": user_id})
    return user.get("language", "en") if user else "en"
