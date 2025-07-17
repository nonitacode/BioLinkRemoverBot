from database.mongo import violations_collection

async def log_violation(chat_id, user_id, reason=""):
    await violations_collection.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"reason": reason}},
        upsert=True
    )

async def clear_violations(chat_id, user_id):
    await violations_collection.delete_one({"chat_id": chat_id, "user_id": user_id})
