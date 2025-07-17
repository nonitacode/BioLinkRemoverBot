# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from config import BOT_NAME

# ✅ Command Handlers
from handlers.commands import start, help, basic, core, moderation, owner, stats

# ✅ Callback Handlers (import as modules to register routes)
import handlers.callbacks.basic
import handlers.callbacks.user
import handlers.callbacks.admin
import handlers.callbacks.developer

# ✅ Group Events & Spam Control
from handlers.group import member_updates
from handlers.spam import group_spam, private_spam

# ✅ Miscellaneous
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
