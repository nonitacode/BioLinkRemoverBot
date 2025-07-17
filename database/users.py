from database.mongo import users_col

async def get_user(user_id: int) -> dict:
    return await users_col.find_one({"user_id": user_id})

async def add_user(user_id: int, first_name: str):
    if not await get_user(user_id):
        await users_col.insert_one({
            "user_id": user_id,
            "first_name": first_name
        })

async def get_all_users():
    return users_col.find()
