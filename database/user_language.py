from database.mongo import user_language_col

async def get_user_language(user_id: int) -> str:
    doc = await user_language_col.find_one({"user_id": user_id})
    return doc["language"] if doc else "en"

async def set_user_language(user_id: int, lang_code: str):
    await user_language_col.update_one(
        {"user_id": user_id},
        {"$set": {"language": lang_code}},
        upsert=True
    )
