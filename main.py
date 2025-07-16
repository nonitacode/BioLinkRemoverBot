# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app  # ✅ Use the existing app instance
from config import BOT_NAME

# ✅ Import all handlers to register them
from handlers.commands import start, help, basic, core, moderation, owner, stats
from handlers.callbacks import start as cb_start, help as cb_help
from handlers.group import member_updates
from handlers.spam import group_spam, private_spam
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
