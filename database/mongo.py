# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pymongo import MongoClient
from config import MONGO_URL

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client.biolinkremoverbot

# MongoDB collections
users_col = db.users
groups_col = db.groups
violation_col = db.violations
whitelist_col = db.whitelist
stats_col = db.stats
language_col = db.language
