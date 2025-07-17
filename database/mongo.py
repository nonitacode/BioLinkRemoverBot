# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["BioLinkRemover"]

users_col = db["users"]
groups_col = db["groups"]
violation_col = db["violations"]
user_language_col = db["user_languages"]
whitelist_col = db["whitelists"]
auth_users_col = db["auth_users"]
