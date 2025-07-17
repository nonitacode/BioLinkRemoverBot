from database.mongo import whitelist_col

async def add_whitelisted_user(chat_id: int, user_id: int):
    await whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"user_ids": user_id}},
        upsert=True
    )

async def remove_whitelisted_user(chat_id: int, user_id: int):
    await whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"user_ids": user_id}}
    )

async def get_whitelisted_users(chat_id: int) -> list:
    doc = await whitelist_col.find_one({"chat_id": chat_id})
    return doc["user_ids"] if doc else []

async def is_user_whitelisted(chat_id: int, user_id: int) -> bool:
    users = await get_whitelisted_users(chat_id)
    return user_id in users
