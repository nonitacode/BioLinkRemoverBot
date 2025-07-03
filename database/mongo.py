from pymongo import MongoClient
from config import MONGO_URL

mongo = MongoClient(MONGO_URL)
db = mongo.LinkScanBot

users = db.users
chats = db.chats
whitelist = db.whitelist

def whitelist_user(chat_id, user_id):
    whitelist.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"chat_id": chat_id, "user_id": user_id}}, upsert=True)

def remove_whitelist(chat_id, user_id):
    whitelist.delete_one({"chat_id": chat_id, "user_id": user_id})

def is_whitelisted(chat_id, user_id):
    return whitelist.find_one({"chat_id": chat_id, "user_id": user_id}) is not None
