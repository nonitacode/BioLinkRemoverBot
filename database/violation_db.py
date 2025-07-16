# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import violation_col
import time

def log_violation(user_id, reason):
    """Logs a violation event into the database."""
    violation_col.insert_one({
        "user_id": user_id,
        "reason": reason,
        "timestamp": time.time()
    })

def get_user_violations(user_id):
    """Retrieves all violations for a specific user."""
    return violation_col.find({"user_id": user_id})
