# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import users_col

def set_user_language(user_id, language_code):
    """Sets the user's preferred language."""
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"preferred_language": language_code}},
        upsert=True
    )

def get_user_language(user_id):
    """Gets the user's preferred language."""
    user = users_col.find_one({"user_id": user_id})
    return user.get("preferred_language") if user else "en"  # Default to English if not set
