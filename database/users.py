# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import users_col

async def store_user_data(user_id: int, username: str = None, first_name: str = ""):
    await users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username": username,
                "first_name": first_name
            }
        },
        upsert=True
    )

async def get_user(user_id: int):
    return await users_col.find_one({"user_id": user_id})

async def get_all_users():
    cursor = users_col.find({})
    return [user async for user in cursor]

async def delete_user(user_id: int):
    await users_col.delete_one({"user_id": user_id})
