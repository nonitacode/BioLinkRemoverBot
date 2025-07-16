# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME
import handlers.commands.core
import handlers.commands.owner
import handlers.commands.moderation
import handlers.callbacks.start
import handlers.misc.message_scan

print(f"{BOT_NAME} is starting...")

bot = Client(
    name="BioLinkRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"}
)

if __name__ == "__main__":
    bot.run()
