# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import whitelist_col

def add_to_whitelist(user_id, username, full_name):
    """Adds a user to the whitelist."""
    whitelist_col.update_one(
        {"user_id": user_id},
        {"$set": {"username": username, "full_name": full_name}},
        upsert=True
    )

def remove_from_whitelist(user_id):
    """Removes a user from the whitelist."""
    whitelist_col.delete_one({"user_id": user_id})

def get_whitelisted_users():
    """Fetch all users from the whitelist."""
    return list(whitelist_col.find({}))
