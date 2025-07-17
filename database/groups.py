# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import groups_col

async def store_group_data(chat_id: int, title: str):
    await groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"title": title}},
        upsert=True
    )

def get_groups_count() -> int:
    return groups_col.count_documents({})
