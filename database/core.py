from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.linkscanbot
whitelist = db.whitelist
violations = db.violations


def is_whitelisted(user_id):
    return whitelist.find_one({"user_id": user_id}) is not None

def add_whitelist(user_id):
    whitelist.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

def remove_whitelist(user_id):
    whitelist.delete_one({"user_id": user_id})

def get_all_whitelist():
    return [x['user_id'] for x in whitelist.find()]

def increment_violations(user_id):
    result = violations.find_one_and_update(
        {"user_id": user_id},
        {"$inc": {"count": 1}},
        upsert=True,
        return_document=True
    )
    return result['count'] if result else 1

def reset_violations(user_id):
    violations.delete_one({"user_id": user_id})
