from database.mongo import users_collection

async def get_user_language(user_id: int) -> str:
    user = await users_collection.find_one({"_id": user_id})
    return user.get("language", "en") if user else "en"

async def set_user_language(user_id: int, language_code: str):
    await users_collection.update_one(
        {"_id": user_id},
        {"$set": {"language": language_code}},
        upsert=True
    )
