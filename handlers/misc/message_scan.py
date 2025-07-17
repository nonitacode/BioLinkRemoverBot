# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.violations import log_violation, get_user_violations
from database.whitelist import get_whitelisted_users
from config import OWNER_ID
from pyrogram.enums import ChatMemberStatus
import re

SPAM_PATTERNS = [
    r"http[s]?://",
    r"@[\w]+",
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

async def check_and_punish(client, message: Message):
    user = message.from_user
    user_id = user.id
    chat_id = message.chat.id

    if user_id == OWNER_ID or await is_admin(client, chat_id, user_id):
        return

    whitelisted_users = await get_whitelisted_users(chat_id)
    if any(u["user_id"] == user_id for u in whitelisted_users):
        return

    await log_violation(chat_id, user_id, "Spam Detected")
    count = await get_user_violations(chat_id, user_id)

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

@Client.on_message(filters.text & filters.group)
async def handle_group_messages(client, message: Message):
    if is_spam(message.text):
        await check_and_punish(client, message)
