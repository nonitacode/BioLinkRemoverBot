# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from database.mongo import violation_col

def log_violation(user_id, reason):
    violation_col.insert_one({"user_id": user_id, "reason": reason})

def get_user_violations(user_id):
    return violation_col.find({"user_id": user_id})

def clear_violations(user_id):
    violation_col.delete_many({"user_id": user_id})
