# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["BioLinkRemover"]

users_collection = db["users"]
groups_col = db["groups"]
violation_col = db["violations"]
user_language_col = db["user_languages"]
whitelists_col = db["whitelists"]
auth_users_collection = db["auth_users"]
warns_col = db["warns"]
