# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB Connection URI
MONGO_URL = os.getenv("MONGO_URL")

# Bot Settings
BOT_NAME = "Bio Link Remover"
BOT_USERNAME = "BioLinkRemoverBot"  # Bot username
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Channel Links
UPDATE_CHANNEL = "GrayBots"
SUPPORT_CHAT = "GrayBotSupport"

# System Monitoring
SYSTEM_MONITOR = {
    'RAM': 'system_ram',
    'CPU': 'system_cpu',
    'STORAGE': 'system_storage'
}

# Command Prefixes
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
