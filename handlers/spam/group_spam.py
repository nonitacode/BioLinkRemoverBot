# utils/spam_checker.py

import re
from config import OWNER_ID
from pyrogram.enums import ChatMemberStatus
from database.whitelist import is_user_whitelisted
from database.violations import log_violation, get_user_violations
from pyrogram.types import Message

SPAM_PATTERNS = [
    r"http[s]?://",
    r"@\w+",
    r"\.com",
    r"t\.me/",
    r"promo"
]

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def is_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

async def check_and_handle_violation(client, message: Message):
    user = message.from_user
    user_id = user.id
    chat_id = message.chat.id

    if user_id == OWNER_ID:
        return

    if await is_admin(client, chat_id, user_id):
        return

    if await is_user_whitelisted(chat_id, user_id):
        return

    await log_violation(chat_id, user_id, reason="Spam Detected")
    count = await get_user_violations(chat_id, user_id)

    try:
        await message.delete()
    except:
        pass

    if count >= 3:
        try:
            await client.restrict_chat_member(chat_id, user_id, permissions={})
            await message.chat.send_message(f"🔇 {user.mention} has been muted after {count} violations.")
        except:
            await message.chat.send_message("❌ Could not mute. Admin rights required.")
    else:
        await message.chat.send_message(f"⚠️ {user.mention}, warning {count}/3.")
