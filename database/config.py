from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.biolinkremoverbot
config_col = db.config

def get_config(chat_id):
    config = config_col.find_one({"chat_id": chat_id})
    if not config:
        config = {"chat_id": chat_id, "warn_limit": 3, "punishment_mode": "mute"}
        config_col.insert_one(config)
    return config

def set_warn_limit(chat_id, limit):
    config_col.update_one({"chat_id": chat_id}, {"$set": {"warn_limit": limit}}, upsert=True)

def set_punishment_mode(chat_id, mode):
    config_col.update_one({"chat_id": chat_id}, {"$set": {"punishment_mode": mode}}, upsert=True)
