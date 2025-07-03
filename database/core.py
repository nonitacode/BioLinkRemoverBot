from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.linkscan  # You can rename 'linkscan' if needed

violations = db.violations
whitelist = db.whitelist
warnings = db.warnings  # Stores last warn message per user per group


# ✅ Whitelist Functions
def is_whitelisted(user_id: int) -> bool:
    return whitelist.find_one({"_id": user_id}) is not None

def add_to_whitelist(user_id: int):
    whitelist.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def remove_from_whitelist(user_id: int):
    whitelist.delete_one({"_id": user_id})

def get_all_whitelist():
    return [u["_id"] for u in whitelist.find()]


# ✅ Violation Count Tracking
def increment_violations(user_id: int) -> int:
    record = violations.find_one({"_id": user_id}) or {"_id": user_id, "count": 0}
    record["count"] += 1
    violations.update_one({"_id": user_id}, {"$set": record}, upsert=True)
    return record["count"]

def get_violations(user_id: int) -> int:
    record = violations.find_one({"_id": user_id})
    return record["count"] if record else 0

def remove_user_record(user_id: int):
    violations.delete_one({"_id": user_id})


# ✅ Warning Message Tracking (Per Chat)
def set_last_warn(chat_id: int, user_id: int, msg_id: int):
    warnings.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"msg_id": msg_id}},
        upsert=True
    )

def get_last_warn(chat_id: int, user_id: int):
    record = warnings.find_one({"chat_id": chat_id, "user_id": user_id})
    return record["msg_id"] if record else None

def delete_last_warn(chat_id: int, user_id: int):
    warnings.delete_one({"chat_id": chat_id, "user_id": user_id})
