# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import whitelist_col

def add_to_whitelist(chat_id, user_id):
    whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

def remove_from_whitelist(chat_id, user_id):
    whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"users": user_id}}
    )

def get_whitelisted_users():
    users = []
    for group in whitelist_col.find({}):
        users.extend(group.get("users", []))
    return [{"user_id": uid} for uid in users]
