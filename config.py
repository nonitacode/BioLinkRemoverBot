# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
OWNER_ID = int(os.getenv("OWNER_ID"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
MAX_VIOLATIONS = int(os.getenv("MAX_VIOLATIONS"))
BOT_NAME = "Bio Link Remover"
