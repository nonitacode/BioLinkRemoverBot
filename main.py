from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from handlers.start import start_handler, callback_handler
from handlers.help import help_handler
from handlers.admin import stats_handler
from handlers.scanner import scan_links
from utils.db import init_db

app = Client(
    "LinkScanBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize database
init_db(MONGO_URL)

# Register handlers
app.add_handler(MessageHandler(start_handler, filters.command("start")))
app.add_handler(MessageHandler(help_handler, filters.command("help")))
app.add_handler(MessageHandler(stats_handler, filters.command(["stats", "about"])))
app.add_handler(CallbackQueryHandler(callback_handler))
app.add_handler(MessageHandler(scan_links, filters.text | filters.caption))

print("Bot is running...")
app.run()
