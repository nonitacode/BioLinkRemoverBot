from database.mongo import groups_col

async def add_group(chat_id: int, chat_title: str):
    await groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"title": chat_title}},
        upsert=True
    )

async def get_all_groups():
    return groups_col.find()
