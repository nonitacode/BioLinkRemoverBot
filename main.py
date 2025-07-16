# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME

# ✅ Import all handlers manually
from handlers.callbacks import start as start_panel, help as help_panel
from handlers.commands import start, help, basic, core, moderation, owner, stats
from handlers.group import member_updates
from handlers.spam import group_spam, private_spam
import handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

bot = Client(
    name="BioLinkRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    bot.run()
