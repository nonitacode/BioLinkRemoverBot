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

LOG_CHANNEL = os.getenv("LOG_CHANNEL")

# Bot Settings
BOT_NAME = "Bio Link Remover"
BOT_USERNAME = "BioLinkRemoverBot"  # Bot username
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Channel Links
UPDATES_CHANNEL = "GrayBots"
SUPPORT_GROUP = "GrayBotSupport"
