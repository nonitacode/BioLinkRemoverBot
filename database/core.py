from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.linkscan
violations = db.violations
whitelist = db.whitelist

def is_whitelisted(user_id: int) -> bool:
    return whitelist.find_one({"_id": user_id}) is not None

def add_to_whitelist(user_id: int):
    whitelist.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def remove_from_whitelist(user_id: int):
    whitelist.delete_one({"_id": user_id})

def get_all_whitelist():
    return [u["_id"] for u in whitelist.find()]

def increment_violations(user_id: int) -> int:
    record = violations.find_one({"_id": user_id}) or {"_id": user_id, "count": 0}
    record["count"] += 1
    violations.update_one({"_id": user_id}, {"$set": record}, upsert=True)
    return record["count"]

def remove_user_record(user_id: int):
    violations.delete_one({"_id": user_id})
