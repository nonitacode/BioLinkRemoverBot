from bot.bot import app
from config import BOT_NAME

# ✅ Command Handlers
from handlers.commands import start, help, basic, core, auth, owner, stats, moderation

# ✅ Callback Query Handlers
import handlers.callbacks.start
import handlers.callbacks.help
import handlers.callbacks.language
import handlers.callbacks.admin
import handlers.callbacks.basic
import handlers.callbacks.developer
import handlers.callbacks.user

# ✅ Group Filters / Scanners
from handlers.group import bio_scan, whitelist, member_updates
from handlers.group.callbacks import unmute

# ✅ Spam Checkers
from handlers.spam import group_spam, private_spam

# ✅ Miscellaneous
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
