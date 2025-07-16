# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import groups_col

def set_admins(chat_id, admin_ids):
    groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"admins": admin_ids}},
        upsert=True
    )

def get_admins(chat_id):
    group = groups_col.find_one({"chat_id": chat_id})
    return group.get("admins", [])

def clear_admins(chat_id):
    groups_col.update_one(
        {"chat_id": chat_id},
        {"$unset": {"admins": ""}}
    )
