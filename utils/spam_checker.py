# utils/spam_checker.py

from database.violations import log_violation, get_user_violations
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from config import OWNER_ID
import re

SPAM_PATTERNS = [
    r"http[s]?://",
    r"@\w+",
    r"\.com",
    r"t\.me/",
    r"promo"
]

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def check_and_handle_violation(client, message: Message):
    user = message.from_user
    user_id = user.id
    chat_id = message.chat.id if message.chat else "private"

    # Log violation
    await log_violation(chat_id, user_id, "Spam Detected")
    count = await get_user_violations(chat_id, user_id)

    if chat_id == "private":
        await message.reply(
            f"⚠️ Detected spam.\nYour message was not accepted.\nWarnings: {count}/3"
        )
    else:
        try:
            await message.delete()
        except:
            pass

        if count >= 3:
            try:
                await client.restrict_chat_member(chat_id, user_id, permissions={})
                await message.reply(f"{user.mention} has been muted after 3 violations.")
            except:
                await message.reply("❌ Could not mute. Admin rights required.")
        else:
            await message.reply(f"{user.mention}, warning {count}/3")
