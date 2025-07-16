# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot import bot
import handlers.start
import handlers.help
import handlers.ping
import handlers.stats
import handlers.violations
import handlers.moderation
import handlers.mute
import handlers.ban
import handlers.unmute
import handlers.admincache
import handlers.spam
import handlers.broadcast
import handlers.private_text

import callbacks.main_buttons
import callbacks.language_callback
import callbacks.command_categories
import callbacks.whitelist_callbacks

print("✅ BioLinkRemoverBot is up and running!")
bot.run()
