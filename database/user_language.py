from database.mongo import user_language_col

def get_user_language(user_id: int) -> str:
    user = user_language_col.find_one({"_id": user_id})
    if user and "language" in user:
        return user["language"]
    return "en"  # default to English

def set_user_language(user_id: int, lang_code: str):
    user_language_col.update_one(
        {"_id": user_id},
        {"$set": {"language": lang_code}},
        upsert=True
    )
