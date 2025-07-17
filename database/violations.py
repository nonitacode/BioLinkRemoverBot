from database.mongo import violation_col

async def log_violation(user_id: int, chat_id: int, reason: str):
    await violation_col.insert_one({
        "user_id": user_id,
        "chat_id": chat_id,
        "reason": reason
    })

async def get_user_violations(user_id: int, chat_id: int) -> int:
    return await violation_col.count_documents({
        "user_id": user_id,
        "chat_id": chat_id
    })

async def reset_violations(user_id: int, chat_id: int):
    await violation_col.delete_many({
        "user_id": user_id,
        "chat_id": chat_id
    })
