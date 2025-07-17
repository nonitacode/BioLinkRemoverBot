# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import groups_col

async def store_group_data(group_id: int, title: str = ""):
    await groups_col.update_one(
        {"group_id": group_id},
        {
            "$set": {
                "title": title
            }
        },
        upsert=True
    )

async def get_group(group_id: int):
    return await groups_col.find_one({"group_id": group_id})

async def delete_group(group_id: int):
    await groups_col.delete_one({"group_id": group_id})

async def get_all_groups():
    cursor = groups_col.find({})
    return [group async for group in cursor]
