# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

import os
from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto
from pyrogram.errors import FloodWait
from config import OWNER_ID, LOG_CHANNEL, BOT_NAME
from bot.bot import bot
from database.user_language_db import get_user_language
from database.violation_db import log_violation, get_user_violations
from database.users_db import store_user_data, store_group_data, get_users_count, get_groups_count
from database.whitelist_db import get_whitelisted_users
from utils.language import get_message
from modules.inline import start_buttons, commands_buttons
from pyrogram.enums import ChatMemberStatus
import asyncio
import re

SPAM_PATTERNS = [r"http[s]?://", r"@[\w]+", r"\.com", r"\.in", r"t\.me/", r"buy", r"sale", r"join", r"promo"]

async def is_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

def is_spam(text: str) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in SPAM_PATTERNS)

async def check_and_handle_violation(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = message.from_user

    # Skip exemptions
    if user_id == OWNER_ID:
        return
    if await is_admin(bot, chat_id, user_id):
        return
    if any(u["user_id"] == user_id for u in get_whitelisted_users()):
        return

    log_violation(user_id, "Spam/Bio detected")
    count = get_user_violations(user_id).count()
    await message.delete()

    if count >= 3:
        try:
            await bot.restrict_chat_member(chat_id, user_id, permissions={})
            await message.reply(f"{user.mention} muted after 3 violations.")
            await bot.send_message(LOG_CHANNEL, f"Muted {user.mention} in {message.chat.title} for 3 violations.")
        except Exception as e:
            await message.reply("Failed to mute the user. Ensure I'm admin.")
            await bot.send_message(LOG_CHANNEL, f"Error muting user: {e}")
    else:
        await message.reply(f"{user.mention}, warning {count}/3 for spam/bio.")

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    user = message.from_user
    chat = message.chat
    store_user_data(user.id, user.username, user.full_name)
    if chat.type in ["group", "supergroup"]:
        store_group_data(chat.id, chat.title)

    lang = get_user_language(user.id)
    welcome_message = get_message(lang, "welcome_message")

    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=welcome_message,
            reply_markup=start_buttons()
        )
    except:
        await message.reply(welcome_message, reply_markup=start_buttons())

    await bot.send_message(LOG_CHANNEL, f"#START by [{user.first_name}](tg://user?id={user.id}) | `{user.id}`")

@bot.on_message(filters.command("help"))
async def help(client, message: Message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")

    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=help_text,
            reply_markup=commands_buttons()
        )
    except:
        await message.reply(help_text, reply_markup=commands_buttons())

    await bot.send_message(LOG_CHANNEL, f"#HELP used by [{message.from_user.first_name}](tg://user?id={message.from_user.id})")

@bot.on_message(filters.command("ping"))
async def ping(client, message: Message):
    await message.reply("✅ Pong! Bot is responsive.")

@bot.on_message(filters.command("alive"))
async def alive(client, message: Message):
    await message.reply("✅ I'm alive and working properly.")

@bot.on_message(filters.command("stats"))
async def stats(client, message: Message):
    users = get_users_count()
    groups = get_groups_count()
    await message.reply(f"📊 **Bot Stats:**\n\n👤 Users: `{users}`\n👥 Groups: `{groups}`")

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

@bot.on_message(filters.text & filters.private)
async def handle_private_text(client, message: Message):
    if is_spam(message.text):
        await check_and_handle_violation(message)

@bot.on_message(filters.text & filters.group)
async def handle_group_text(client, message: Message):
    if is_spam(message.text):
        await check_and_handle_violation(message)

@bot.on_chat_member_updated()
async def log_new_member(client, event):
    if event.new_chat_member and event.new_chat_member.user.is_bot:
        return
    if event.new_chat_member:
        user = event.new_chat_member.user
        await bot.send_message(
            LOG_CHANNEL,
            f"#JOINED\nUser: [{user.first_name}](tg://user?id={user.id})\nChat: {event.chat.title}"
        )
    elif event.old_chat_member and event.old_chat_member.status != "left" and event.new_chat_member.status == "left":
        user = event.old_chat_member.user
        await bot.send_message(
            LOG_CHANNEL,
            f"#LEFT\nUser: [{user.first_name}](tg://user?id={user.id})\nChat: {event.chat.title}"
        )
