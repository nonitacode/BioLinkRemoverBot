# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import users_col, groups_col

def store_user_data(user_id, username, full_name):
    """Store user data when they interact with the bot."""
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"username": username, "full_name": full_name}},
        upsert=True
    )

def store_group_data(chat_id, group_name):
    """Store group data."""
    groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"group_name": group_name}},
        upsert=True
    )

def get_users_count():
    """Get the count of all users stored in the database."""
    return users_col.count_documents({})

def get_groups_count():
    """Get the count of all groups (chats) the bot is in."""
    return groups_col.count_documents({})
