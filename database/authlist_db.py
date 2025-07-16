# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import groups_col

def add_to_group_authlist(chat_id, user_id, username):
    """Add a user to the group's authlist."""
    groups_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"authlist": {"user_id": user_id, "username": username}}},
        upsert=True
    )

def remove_from_group_authlist(chat_id, user_id):
    """Remove a user from the group's authlist."""
    groups_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"authlist": {"user_id": user_id}}}
    )

def get_group_authlist(chat_id):
    """Fetch the authlist for a specific group."""
    group = groups_col.find_one({"chat_id": chat_id})
    return group.get("authlist", []) if group else []
