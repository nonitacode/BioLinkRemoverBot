import logging
from pyrogram import Client
from pyrogram.types import Message
import handlers  # imports all handler modules
from config import API_ID, API_HASH, BOT_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# Initialize bot client
app = Client(
    "LinkScanBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Load all handlers via import (decorators already attached)
from handlers import (
    message_scan,
    join_scan,
    admin_commands,
    settings,
    broadcast,
    help,
    start,
    about_stats
)

# Start the bot
if __name__ == "__main__":
    LOGGER.info("🚀 LinkScanBot is starting...")
    app.run()
