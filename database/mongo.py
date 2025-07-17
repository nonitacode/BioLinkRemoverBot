# mongo.py

from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["BioLinkRemover"]

users_collection = db["users"]
groups_col = db["groups"]
violation_col = db["violations"]
user_language_col = db["user_languages"]
whitelists_col = db["whitelists"]   # ✅ FIXED: renamed for correct import
auth_users_collection = db["auth_users"]
warns_col = db["warns"]
