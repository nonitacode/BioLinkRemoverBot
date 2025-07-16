# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import bot
from database.violations import log_violation, get_user_violations

@bot.on_message(filters.command("warn"))
async def warn_command(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to warn.")
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "Warned manually")
    count = get_user_violations(user_id).count()
    await message.reply(f"User warned. Total warnings: {count}")

@bot.on_message(filters.command("mute"))
async def mute_command(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute.")
    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(message.chat.id, user_id, permissions={})
        await message.reply("User muted.")
        log_violation(user_id, "Muted manually")
    except:
        await message.reply("Failed to mute. Make sure I'm admin.")

@bot.on_message(filters.command("ban"))
async def ban_command(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to ban.")
    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply("User banned.")
        log_violation(user_id, "Banned manually")
    except:
        await message.reply("Failed to ban. Make sure I'm admin.")
