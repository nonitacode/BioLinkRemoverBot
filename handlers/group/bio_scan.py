# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.violations import log_violation, get_user_violations, clear_violations
from database.whitelist import is_user_whitelisted
from utils.language import get_message
from config import OWNER_ID
from pyrogram.types import ChatMemberStatus
import re

SPAM_PATTERNS = [r"http[s]?://", r"@[\w]+", r"\.com", r"t\.me/", r"promo"]

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def is_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

@Client.on_message(filters.group & filters.text)
async def scan_user_bio(client, message: Message):
    user = message.from_user
    if not user or user.is_bot:
        return

    chat_id = message.chat.id
    user_id = user.id

    # Skip if owner or admin
    if user_id == OWNER_ID or await is_admin(client, chat_id, user_id):
        return

    # Skip if whitelisted
    if await is_user_whitelisted(chat_id, user_id):
        return

    bio = user.bio or ""
    if not is_spam(bio):
        return

    # Log warning
    log_violation(chat_id, user_id, "Bio contains link/username")
    count = get_user_violations(chat_id, user_id).count()

    lang = "en"
    try:
        lang = (await client.db.get_user_language(user_id)) or "en"
    except:
        pass

    await message.delete()

    if count >= 3:
        try:
            await client.restrict_chat_member(chat_id, user_id, permissions={})
            await message.reply(
                get_message(lang, "user_muted").format(user=user.mention),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔓 Unmute", callback_data=f"unmute_{user_id}")]
                ])
            )
        except:
            await message.reply("❌ Unable to mute user.")
    else:
        await message.reply(
            get_message(lang, "warn_user").format(user=user.mention, count=count)
        )
