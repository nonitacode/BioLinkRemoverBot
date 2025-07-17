# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.whitelist import add_to_whitelist, remove_from_whitelist
from database.violations import clear_violations
from config import OWNER_ID

@Client.on_message(filters.command("allow") & filters.group)
async def allow_user(_, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ You are not authorized to use this command.")
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user to allow them.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    await add_to_whitelist(chat_id, user_id)
    await clear_violations(user_id)

    await message.reply(f"✅ Allowed [{user_id}](tg://user?id={user_id}) and cleared their warnings.")

@Client.on_message(filters.command("remove") & filters.group)
async def remove_user(_, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ You are not authorized to use this command.")
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user to remove them from whitelist.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    await remove_from_whitelist(chat_id, user_id)
    await message.reply(f"🚫 Removed [{user_id}](tg://user?id={user_id}) from whitelist.")
