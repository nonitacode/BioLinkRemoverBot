from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client.link_scan_db

# Users and whitelist collections
users = db.users
chats = db.chats
whitelist = db.whitelist

def is_whitelisted(chat_id, user_id):
    return bool(whitelist.find_one({"chat_id": chat_id, "user_id": user_id}))

def add_whitelist(chat_id, user_id):
    whitelist.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"chat_id": chat_id, "user_id": user_id}},
        upsert=True
    )

def remove_whitelist(chat_id, user_id):
    whitelist.delete_one({"chat_id": chat_id, "user_id": user_id})
