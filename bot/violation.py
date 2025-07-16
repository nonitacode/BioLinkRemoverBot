# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from bot.bot import bot  # Importing the initialized bot object
from pyrogram import filters
from database.violation_db import log_violation

@bot.on_message(filters.command("warn"))
async def warn_user(client, message):
    """Handles the /warn command and warns a user."""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User warned")
    await message.reply("User has been warned.")

@bot.on_message(filters.command("ban"))
async def ban_user(client, message):
    """Handles the /ban command and bans a user."""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User banned")
    await message.reply("User has been banned from the group.")

@bot.on_message(filters.command("mute"))
async def mute_user(client, message):
    """Handles the /mute command and mutes a user."""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User muted")
    await message.reply("User has been muted.")
