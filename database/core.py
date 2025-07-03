from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.link_scan

whitelist_col = db.whitelist
violations_col = db.violations
config_col = db.config
warn_cache_col = db.warn_cache
backup_col = db.violation_backup


def add_to_whitelist(user_id):
    whitelist_col.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def remove_from_whitelist(user_id):
    whitelist_col.delete_one({"_id": user_id})

def is_whitelisted(user_id):
    return whitelist_col.find_one({"_id": user_id}) is not None

def get_all_whitelist():
    return [doc["_id"] for doc in whitelist_col.find()]

def increment_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return violations_col.find_one_and_update(
        {"_id": key}, {"$inc": {"count": 1}}, upsert=True, return_document=True
    )["count"]

def get_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = violations_col.find_one({"_id": key})
    return doc["count"] if doc else 0

def remove_user_record(user_id):
    violations_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    warn_cache_col.delete_many({"_id": {"$regex": f":{user_id}$"}})
    backup_col.delete_many({"_id": {"$regex": f":{user_id}$"}})

def delete_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    warn_cache_col.delete_one({"_id": key})

def save_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = violations_col.find_one({"_id": key})
    if doc:
        backup_col.update_one({"_id": key}, {"$set": doc}, upsert=True)

def restore_old_violations(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    doc = backup_col.find_one({"_id": key})
    if doc:
        violations_col.replace_one({"_id": key}, doc, upsert=True)
        backup_col.delete_one({"_id": key})

def get_last_warn(chat_id, user_id):
    key = f"{chat_id}:{user_id}"
    return warn_cache_col.find_one({"_id": key})
