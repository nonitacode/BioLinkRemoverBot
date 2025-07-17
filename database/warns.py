# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import warns_col

def add_warn(user_id: int, chat_id: int, reason: str = "Violation"):
    warns_col.insert_one({
        "user_id": user_id,
        "chat_id": chat_id,
        "reason": reason
    })

def get_warns_count(user_id: int, chat_id: int) -> int:
    return warns_col.count_documents({
        "user_id": user_id,
        "chat_id": chat_id
    })

def reset_warns(user_id: int, chat_id: int):
    warns_col.delete_many({
        "user_id": user_id,
        "chat_id": chat_id
    })

def get_all_warns(chat_id: int):
    return list(warns_col.find({"chat_id": chat_id}))
