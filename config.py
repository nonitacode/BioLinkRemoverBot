import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# MongoDB
MONGO_URL = getenv("MONGO_URL", None)

# Bot Settings
MAX_VIOLATIONS = int(getenv("MAX_VIOLATIONS", 5))  # Number of violations before action
LOG_CHANNEL = int(getenv("LOG_CHANNEL", 0))        # Channel ID for logging actions

# Bot Identity
BOT_NAME = "Bio Link Remover"
OWNER_ID = int(getenv("OWNER_ID", "123456789"))
