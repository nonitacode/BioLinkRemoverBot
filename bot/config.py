# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration from environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")

# Bot Identity
BOT_NAME = "Bio Link Remover"
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# MongoDB
MONGO_URL = os.getenv("MONGO_URL")

# Bot Commands
COMMAND_PREFIXES = {
    "start": "/start",
    "ping": "/ping",
    "alive": "/alive",
    "stats": "/stats",
    "warn": "/warn",
    "profile": "/profile",
    "addauth": "/addauth",
    "removeauth": "/removeauth",
    "ban": "/ban",
    "mute": "/mute",
    "unmute": "/unmute",
    "spam": "/spam",
    "broadcast": "/broadcast",
    "config": "/config"
}
