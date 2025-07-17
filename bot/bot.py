from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "BioLinkRemoverBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)
