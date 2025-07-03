import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL", None)
MAX_VIOLATIONS = int(getenv("MAX_VIOLATIONS", 3))
LOG_CHANNEL = int(getenv("LOG_CHANNEL", 0))
