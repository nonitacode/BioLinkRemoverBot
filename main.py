# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from config import BOT_NAME

# ✅ Command Handlers (You can customize this as per your actual file structure)
from handlers.commands import start, help, basic, core, moderation, owner, stats

# ✅ Callback Handlers – organized by category
from handlers.callbacks import callback_basic
from handlers.callbacks import callback_user
from handlers.callbacks import callback_admin
from handlers.callbacks import callback_developer

# ✅ Group Updates & Spam Control
from handlers.group import member_updates
from handlers.spam import group_spam, private_spam

# ✅ Miscellaneous (e.g. message scanner)
from handlers.misc import message_scan

print(f"{BOT_NAME} is starting...")

if __name__ == "__main__":
    app.run()
