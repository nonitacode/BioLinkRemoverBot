# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

import logging
from config import LOG_CHANNEL
from bot.bot import bot

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_console(message: str):
    logging.info(message)

async def log_to_channel(message: str):
    try:
        await bot.send_message(LOG_CHANNEL, message)
    except Exception as e:
        logging.error(f"Logging to channel failed: {e}")
