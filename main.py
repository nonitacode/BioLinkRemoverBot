# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME

# ✅ Import all handlers manually
from handlers.commands import start, help
from handlers.callbacks import start as start_cb, help as help_cb
import handlers.commands.core
import handlers.commands.owner
import handlers.commands.moderation
import handlers.misc.message_scan

print(f"{BOT_NAME} is starting...")

bot = Client(
    name="BioLinkRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    bot.run()
