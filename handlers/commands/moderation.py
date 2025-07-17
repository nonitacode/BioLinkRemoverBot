# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from database.violations import log_violation, get_user_violations  # ✅ Should be async
from config import LOG_CHANNEL

@Client.on_message(filters.command("warn") & filters.group)
async def warn(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user to warn them.")

    user_id = message.reply_to_message.from_user.id

    await log_violation(user_id, "Manual Warning")  # ✅ Awaited
    count = await get_user_violations(user_id)      # ✅ Awaited
    total = len(count)

    await message.reply(f"⚠️ Warning issued. Total: {total}/3")

@Client.on_message(filters.command("mute") & filters.group)
async def mute(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("🔇 Reply to a user to mute them.")

    user_id = message.reply_to_message.from_user.id

    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        await log_violation(user_id, "Manually Muted")
        await message.reply("🔇 User has been muted.")
    except Exception as e:
        await message.reply(f"❌ Failed to mute: {e}")

@Client.on_message(filters.command("ban") & filters.group)
async def ban(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("⛔ Reply to a user to ban them.")

    user_id = message.reply_to_message.from_user.id

    try:
        await message.chat.ban_member(user_id)
        await log_violation(user_id, "Manually Banned")
        await message.reply("⛔ User has been banned.")
    except Exception as e:
        await message.reply(f"❌ Failed to ban: {e}")
