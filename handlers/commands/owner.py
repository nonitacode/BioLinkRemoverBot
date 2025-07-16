# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.whitelist import add_to_whitelist, remove_from_whitelist
from database.violations import clear_violations
from config import OWNER_ID

@Client.on_message(filters.command("allow"))
async def allow_user(_, message: Message):
    if not message.from_user.id == OWNER_ID:
        return
    if not message.reply_to_message:
        return await message.reply("Reply to a user to allow them.")
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    add_to_whitelist(chat_id, user_id)
    clear_violations(user_id)
    await message.reply(f"✅ Allowed {user_id} and cleared warnings.")

@Client.on_message(filters.command("remove"))
async def remove_user(_, message: Message):
    if not message.from_user.id == OWNER_ID:
        return
    if not message.reply_to_message:
        return await message.reply("Reply to a user to remove from whitelist.")
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    remove_from_whitelist(chat_id, user_id)
    await message.reply(f"🚫 Removed {user_id} from whitelist.")
