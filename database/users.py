# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import users_col

def store_user_data(user_id, username, full_name):
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"username": username, "full_name": full_name}},
        upsert=True
    )

def get_users_count():
    return users_col.count_documents({})
