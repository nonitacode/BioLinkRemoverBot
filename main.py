# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from bot.bot import bot
from config import OWNER_ID, LOG_CHANNEL
from database.users_db import store_user_data
from database.stats_db import get_bot_stats
from database.authlist_db import get_group_authlist, add_to_group_authlist
from database.violation_db import log_violation, get_user_violations, clear_user_violations
from database.user_language_db import get_user_language
from database.whitelist_db import add_to_whitelist
from utils.language import get_message
from utils.helpers import is_user_admin, mute_user
from modules.inline import start_buttons, commands_buttons

MAX_WARNINGS = 3

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    lang = get_user_language(user.id)
    welcome_message = get_message(lang, "welcome_message")
    await message.reply(welcome_message, reply_markup=start_buttons())

@bot.on_message(filters.command("help"))
async def help(client, message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")
    await message.reply(help_text, reply_markup=commands_buttons())

@bot.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply("✅ Pong!")

@bot.on_message(filters.command("alive"))
async def alive(client, message):
    await message.reply("✅ I'm alive and operational!")

@bot.on_message(filters.command("stats"))
async def stats(client, message):
    users, groups = get_bot_stats()
    await message.reply(f"📊 Stats:\nUsers: {users}\nGroups: {groups}")

@bot.on_message(filters.command("warn"))
async def manual_warn(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ Reply to a user's message to warn them.")
    
    victim = message.reply_to_message.from_user
    if victim.id == OWNER_ID or await is_user_admin(message.chat.id, victim.id):
        return await message.reply("⚠️ Cannot warn admins or owner.")
    
    log_violation(victim.id, "Manual Warning")
    warnings = list(get_user_violations(victim.id))
    
    await message.reply(f"⚠️ {victim.mention} warned! Total warnings: {len(warnings)}/{MAX_WARNINGS}")
    await bot.send_message(LOG_CHANNEL, f"🚨 Warned {victim.mention} in {message.chat.title}")

    if len(warnings) >= MAX_WARNINGS:
        await mute_user(client, message.chat.id, victim.id)
        await message.reply(f"🔇 {victim.mention} has been muted due to repeated violations.")

@bot.on_message(filters.command("allow"))
async def allow_user(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ Reply to a user to allow them.")
    
    user = message.reply_to_message.from_user
    chat_id = message.chat.id
    add_to_group_authlist(chat_id, user.id, user.username or "")
    clear_user_violations(user.id)
    add_to_whitelist(user.id, user.username or "", user.first_name)

    await message.reply(f"✅ {user.mention} has been allowed in this group. All violations cleared.")
    await bot.send_message(LOG_CHANNEL, f"🛡️ {user.mention} added to authlist in {message.chat.title}")
