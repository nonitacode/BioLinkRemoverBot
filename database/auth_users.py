# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import auth_users_col

def add_auth_user(user_id: int):
    auth_users_col.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

def remove_auth_user(user_id: int):
    auth_users_col.delete_one({"user_id": user_id})

def get_auth_users() -> list:
    return [doc["user_id"] for doc in auth_users_col.find({}, {"_id": 0, "user_id": 1})]

def is_auth_user(user_id: int) -> bool:
    return auth_users_col.count_documents({"user_id": user_id}) > 0
