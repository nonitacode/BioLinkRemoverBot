# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import auth_users_col

def add_auth_user(group_id: int, user_id: int):
    """Add user to the group's authorized list."""
    auth_users_col.update_one(
        {"group_id": group_id},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

def remove_auth_user(group_id: int, user_id: int):
    """Remove user from the group's authorized list."""
    auth_users_col.update_one(
        {"group_id": group_id},
        {"$pull": {"users": user_id}}
    )

def get_auth_users(group_id: int):
    """Get the list of authorized users for the group."""
    group = auth_users_col.find_one({"group_id": group_id})
    return group["users"] if group and "users" in group else []

def is_user_authorized(group_id: int, user_id: int) -> bool:
    """Check if the user is authorized in the group."""
    group = auth_users_col.find_one({"group_id": group_id})
    return user_id in group.get("users", []) if group else False
