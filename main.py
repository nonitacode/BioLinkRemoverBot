from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import message_scan, join_scan, admin_commands, settings

app = Client("LinkScanBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers
app.add_handler(message_scan.link_checker)
app.add_handler(join_scan.bio_checker)
app.add_handler(admin_commands.admin_cmds)
app.add_handler(settings.settings_cmd)

if __name__ == "__main__":
    print("🤖 LinkScanBot Started!")
    app.run()
