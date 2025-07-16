# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.mongo import stats_col

def update_bot_stats(users_count, groups_count):
    """Update the bot's statistics in the database."""
    stats_col.update_one(
        {"_id": "stats"},
        {"$set": {"users_count": users_count, "groups_count": groups_count}},
        upsert=True
    )

def get_bot_stats():
    """Get the current bot statistics (users, groups)."""
    stats = stats_col.find_one({"_id": "stats"})
    if stats:
        return stats.get("users_count", 0), stats.get("groups_count", 0)
    return 0, 0
