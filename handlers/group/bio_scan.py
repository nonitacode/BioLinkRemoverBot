# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import re
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from database.violations import log_violation
from database.whitelist import is_user_whitelisted
from utils.language import get_message
from config import OWNER_ID

# Spam detection patterns
SPAM_PATTERNS = [
    r"http[s]?://",
    r"@\w+",
    r"\.com",
    r"t\.me/",
    r"promo"
]

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def is_admin(client: Client, chat_id: int, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

@Client.on_message(filters.group & filters.text)
async def scan_user_bio(client: Client, message: Message):
    user = message.from_user
    if not user or user.is_bot:
        return

    chat_id = message.chat.id
    user_id = user.id

    # Ignore bot owner and admins
    if user_id == OWNER_ID or await is_admin(client, chat_id, user_id):
        return

    # Skip if whitelisted
    if await is_user_whitelisted(chat_id, user_id):
        return

    # Get bio info safely
    try:
        user_info = await client.get_users(user_id)
        bio = user_info.bio or ""
    except:
        bio = ""

    # Scan both bio and message content
    if is_spam(bio) or is_spam(message.text):
        await log_violation(chat_id, user_id, reason="Bio or message contains spam.")

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🚫 Ban", callback_data=f"ban_{chat_id}_{user_id}")],
            [InlineKeyboardButton("✅ Ignore", callback_data=f"ignore_{chat_id}_{user_id}")]
        ])

        await message.reply_text(
            f"⚠️ <b>Suspicious content detected</b> from <a href='tg://user?id={user_id}'>{user.first_name}</a>\n\n"
            f"<b>Bio:</b> <code>{bio}</code>\n"
            f"<b>Message:</b> <code>{message.text}</code>",
            reply_markup=buttons,
            disable_web_page_preview=True
        )
