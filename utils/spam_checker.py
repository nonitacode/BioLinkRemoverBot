import re
from config import OWNER_ID, LOG_CHANNEL, MAX_VIOLATIONS
from bot.bot import app
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from database.violations import log_violation, get_user_violations
from database.whitelist import get_whitelisted_users

SPAM_PATTERNS = [
    r"http[s]?://", r"@[\w]+", r"\.com", r"\.in", r"t\.me/",
    r"buy", r"sale", r"join", r"promo"
]

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

    if await is_admin(app, chat_id, user_id):
        return

    whitelisted = await get_whitelisted_users(chat_id)
    if user_id in whitelisted:
        return

    await log_violation(user_id, chat_id, "Spam/Bio Detected")
    count = await get_user_violations(user_id, chat_id)

    await message.delete()

    if count >= MAX_VIOLATIONS:
        try:
            await app.restrict_chat_member(chat_id, user_id, permissions={})
            await app.send_message(chat_id, f"{user.mention} muted after {MAX_VIOLATIONS} violations.")
            await app.send_message(LOG_CHANNEL, f"🚫 Muted [{user.first_name}](tg://user?id={user.id}) in {message.chat.title} for spam.")
        except Exception as e:
            await app.send_message(chat_id, "⚠️ Failed to mute user. Make sure I’m admin.")
            await app.send_message(LOG_CHANNEL, f"❌ Error muting user: {e}")
    else:
        await app.send_message(chat_id, f"⚠️ {user.mention}, warning {count}/{MAX_VIOLATIONS} for spam.")
