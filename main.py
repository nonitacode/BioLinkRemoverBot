# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from config import BOT_NAME

# ✅ Command Handlers
from handlers.commands import start, help, basic, core, moderation, owner, stats

# ✅ Callback Handlers (explicitly importing modules)
import handlers.callbacks.start
import handlers.callbacks.help
import handlers.callbacks.basic
import handlers.callbacks.user
import handlers.callbacks.admin
import handlers.callbacks.developer
import handlers.callbacks.language

# ✅ Group & Spam
from handlers.group import member_updates
from handlers.spam import group_spam, private_spam

# ✅ Miscellaneous
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
