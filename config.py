import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
MAX_VIOLATIONS = int(os.getenv("MAX_VIOLATIONS", 3))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
