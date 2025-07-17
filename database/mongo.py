# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["BioLinkRemover"]

users_collection = db["users"]
groups_collection = db["groups"]
violations_collection = db["violations"]
user_language_collection = db["user_languages"]
whitelist_collection = db["whitelists"]
auth_users_collection = db["auth_users"]
warns_collection = db["warns"]
