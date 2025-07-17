# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import whitelist_col

def add_to_whitelist(chat_id: int, user_id: int):
    whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

def remove_from_whitelist(chat_id: int, user_id: int):
    whitelist_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"users": user_id}}
    )

def get_whitelisted_users(chat_id: int) -> list:
    group = whitelist_col.find_one({"chat_id": chat_id}) or {}
    return group.get("users", [])

def is_user_whitelisted(chat_id: int, user_id: int) -> bool:
    group = whitelist_col.find_one({"chat_id": chat_id})
    return user_id in group.get("users", []) if group else False
