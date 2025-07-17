# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import users_col, user_language_col

async def store_user_data(user_id: int, first_name: str = "", username: str = ""):
    await users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "first_name": first_name,
                "username": username
            }
        },
        upsert=True
    )

async def get_user(user_id: int):
    return await users_col.find_one({"user_id": user_id})

async def set_user_language(user_id: int, language_code: str):
    await user_language_col.update_one(
        {"user_id": user_id},
        {"$set": {"language_code": language_code}},
        upsert=True
    )

def get_user_language(user_id: int) -> str:
    lang = user_language_col.find_one({"user_id": user_id})
    return lang["language_code"] if lang and "language_code" in lang else "en"
