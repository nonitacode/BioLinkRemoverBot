# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import users_col

def store_user_data(user_id, username, full_name):
    """Stores user data in the database."""
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"username": username, "full_name": full_name}},
        upsert=True
    )

def get_user_data(user_id):
    """Fetches user data from the database."""
    return users_col.find_one({"user_id": user_id})

def store_user_language(user_id, language):
    """Stores the user's language preference."""
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"language": language}},
        upsert=True
    )

def get_user_language(user_id):
    """Fetches the user's language preference."""
    user = users_col.find_one({"user_id": user_id})
    return user.get("language") if user else None
