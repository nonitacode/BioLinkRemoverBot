# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from config import BOT_NAME

# ✅ Callback Query Handlers
import handlers.callbacks.start
import handlers.callbacks.help
import handlers.callbacks.language
import handlers.callbacks.admin
import handlers.callbacks.basic
import handlers.callbacks.developer
import handlers.callbacks.user

# ✅ Command Handlers
from handlers.commands import start, help, basic, core, auth, owner, stats, moderation
import handlers.commands.allow
import handlers.commands.warn
import handlers.commands.mute
import handlers.commands.ban
import handlers.commands.bioscan

# ✅ Group Filters / Scanners
from handlers.group import bio_scan, whitelist, member_updates
from handlers.group.callbacks import unmute

# ✅ Spam Checkers
from handlers.spam import group_spam

# ✅ Miscellaneous
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
