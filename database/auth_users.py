from database.mongo import auth_users_col

async def is_auth(user_id: int) -> bool:
    return bool(await auth_users_col.find_one({"user_id": user_id}))

async def add_auth(user_id: int):
    if not await is_auth(user_id):
        await auth_users_col.insert_one({"user_id": user_id})

async def remove_auth(user_id: int):
    await auth_users_col.delete_one({"user_id": user_id})

async def get_all_auth_users():
    return [doc["user_id"] async for doc in auth_users_col.find()]
