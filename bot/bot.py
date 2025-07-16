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

# Define bot start handler (startup logic)
async def on_start(client):
    """This function will be called when the bot starts."""
    log("Bot started successfully")

# Shutdown handling function
async def on_shutdown(client):
    """This function will be called when the bot is shutting down."""
    log("Bot shutting down...")

# Define a handler to stop the bot and call shutdown logic
async def stop_bot(client):
    """Stops the bot and triggers shutdown handling."""
    await client.stop()
    await on_shutdown(client)

# Start the bot and handle shutdown logic
if __name__ == "__main__":
    log("Starting BioLinkRemoverBot...")
    
    # Attach the on_start and on_shutdown functions to handle the startup and shutdown events
    bot.add_handler(on_start)  # Add start handler
    bot.add_handler(on_shutdown)  # Add shutdown handler
    
    # Start the bot with a correct run method that will handle shutdown events.
    bot.run()
