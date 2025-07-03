from pymongo import MongoClient

db = None

def init_db(uri):
    global db
    client = MongoClient(uri)
    db = client.linkscanbot

async def is_whitelisted(user_id: int, chat_id: int) -> bool:
    return bool(
        db.whitelist.find_one({
            "$or": [{"user_id": user_id}, {"chat_id": chat_id}]
        })
    )

async def get_stats():
    group_count = db.whitelist.distinct("chat_id")
    user_count = db.whitelist.distinct("user_id")
    return len(group_count), len(user_count)
