# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from bot.logger import log

# Initialize the bot client
bot = Client(
    "BioLinkRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define bot startup
@bot.on_start
async def on_start(client):
    log("Bot started successfully")

# Define the shutdown handler
@bot.on_shutdown
async def on_shutdown(client):
    log("Bot shutting down")

# Run the bot
bot.run()
