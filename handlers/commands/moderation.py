# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.violations import log_violation, get_user_violations
from pyrogram.enums import ChatPermissions

@Client.on_message(filters.command("warn"))
async def warn(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to warn them.")
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "Manual Warning")
    count = get_user_violations(user_id).count()
    await message.reply(f"⚠️ Warning issued. Total: {count}/3")

@Client.on_message(filters.command("mute"))
async def mute(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute them.")
    user_id = message.reply_to_message.from_user.id
    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        log_violation(user_id, "Manually Muted")
        await message.reply("🔇 User has been muted.")
    except Exception:
        await message.reply("❌ Failed to mute. Make sure I’m an admin.")

@Client.on_message(filters.command("ban"))
async def ban(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to ban them.")
    user_id = message.reply_to_message.from_user.id
    try:
        await message.chat.ban_member(user_id)
        log_violation(user_id, "Manually Banned")
        await message.reply("⛔ User has been banned.")
    except Exception:
        await message.reply("❌ Failed to ban. Ensure I have ban rights.")
