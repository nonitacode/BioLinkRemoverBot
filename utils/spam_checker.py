# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import re
from config import OWNER_ID, LOG_CHANNEL, MAX_VIOLATIONS
from bot.bot import app
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from database.violations import log_violation, get_user_violations
from database.whitelist import get_whitelisted_users

SPAM_PATTERNS = [r"http[s]?://", r"@[\w]+", r"\.com", r"\.in", r"t\.me/", r"buy", r"sale", r"join", r"promo"]

async def is_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def check_and_handle_violation(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = message.from_user

    if user_id == OWNER_ID:
        return
    if await is_admin(bot, chat_id, user_id):
        return
    if any(u["user_id"] == user_id for u in get_whitelisted_users()):
        return

    log_violation(user_id, "Spam/Bio detected")
    count = get_user_violations(user_id).count()
    await message.delete()

    if count >= MAX_VIOLATIONS:
        try:
            await app.restrict_chat_member(chat_id, user_id, permissions={})
            await message.reply(f"{user.mention} muted after {MAX_VIOLATIONS} violations.")
            await app.send_message(LOG_CHANNEL, f"Muted {user.mention} in {message.chat.title} for {MAX_VIOLATIONS} violations.")
        except Exception as e:
            await message.reply("Failed to mute the user. Ensure I'm admin.")
            await app.send_message(LOG_CHANNEL, f"Error muting user: {e}")
    else:
        await message.reply(f"{user.mention}, warning {count}/{MAX_VIOLATIONS} for spam/bio.")
