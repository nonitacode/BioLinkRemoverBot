from database.mongo import violation_col

def log_violation(chat_id, user_id, reason):
    violation_col.insert_one({"chat_id": chat_id, "user_id": user_id, "reason": reason})

def get_user_violations(chat_id, user_id):
    return violation_col.find({"chat_id": chat_id, "user_id": user_id})

def clear_violations(chat_id, user_id):
    violation_col.delete_many({"chat_id": chat_id, "user_id": user_id})
