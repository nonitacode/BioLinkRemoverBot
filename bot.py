from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import start, help, admin, moderation

app = Client("linkscanbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

start.init(app)
help.init(app)
admin.init(app)
moderation.init(app)

print("Bot is running...")
app.run()
