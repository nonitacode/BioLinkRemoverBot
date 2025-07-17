# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from config import BOT_NAME

# ✅ Command Handlers
from handlers.commands import auth, basic, core, core, help, moderation, owner, start, stats
from handlers.group.callbacks import unmute
from handlers.group import bio_scan, whitelist, member_updates

# ✅ Callback Handlers (explicitly importing modules)
import handlers.callbacks.admin
import handlers.callbacks.basic
import handlers.callbacks.developer
import handlers.callbacks.help
import handlers.callbacks.language
import handlers.callbacks.start
import handlers.callbacks.user

# ✅ Group & Spam
from handlers.spam import group_spam, private_spam

# ✅ Miscellaneous
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
