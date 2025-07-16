# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.group_admins_db import get_admins
from config import OWNER_ID
from database.authlist_db import get_group_authlist

@bot.on_message(filters.text)
async def detect_spam(client, message: Message):
    if not message.chat or not message.from_user:
        return

    user_id = message.from_user.id
    chat_id = message.chat.id

    # Skip if bot owner
    if user_id == OWNER_ID:
        return

    # Skip if in whitelist
    whitelist = get_group_authlist(chat_id)
    if any(w["user_id"] == user_id for w in whitelist):
        return

    # Skip if admin (from cache)
    admins = get_admins(chat_id)
    if user_id in admins:
        return

    # Scan message
    text = message.text.lower()
    if any(keyword in text for keyword in ["http", "@", "promo", "buy", "sale"]):
        await message.delete()
        log_violation(user_id, "Spam message detected")
        await message.reply("🚫 Message deleted due to potential spam.")
