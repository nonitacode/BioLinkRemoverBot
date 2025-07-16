# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import user_language_col

def get_user_language(user_id):
    data = user_language_col.find_one({"user_id": user_id})
    return data["lang_code"] if data else "en"

def set_user_language(user_id, lang_code):
    user_language_col.update_one(
        {"user_id": user_id},
        {"$set": {"lang_code": lang_code}},
        upsert=True
    )
