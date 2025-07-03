from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME

app = Client(BOT_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import all handlers
from handlers import start, help, admin, moderation, join_filter

start.init(app)
help.init(app)
admin.init(app)
moderation.init(app)
join_filter.init(app)

print("Bot started!")
app.run()
