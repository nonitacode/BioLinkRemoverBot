# main.py

from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from bot.bot import bot
from config import OWNER_ID
from database.users_db import store_user_data
from database.stats_db import get_bot_stats
from database.violation_db import log_violation
from database.user_language_db import get_user_language
from utils.language import get_message
from modules.inline import start_buttons, commands_buttons
from bot.logger import log, error_log

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    lang = get_user_language(user.id)
    welcome_text = get_message(lang, "welcome_message")
    try:
        await message.reply_photo(
            photo="assets/biolinkremoverbot.png",
            caption=welcome_text,
            reply_markup=start_buttons()
        )
        log(f"/start used by {user.id}")
    except Exception as e:
        error_log(f"Failed to send start image: {e}")
        await message.reply(welcome_text, reply_markup=start_buttons())

@bot.on_message(filters.command("help"))
async def help(client, message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")
    await message.reply(help_text, reply_markup=commands_buttons())
    log(f"/help used by {message.from_user.id}")

@bot.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply("✅ Pong!")
    log(f"/ping used by {message.from_user.id}")

@bot.on_message(filters.command("alive"))
async def alive(client, message):
    await message.reply("✅ I am alive and running!")
    log(f"/alive used by {message.from_user.id}")

@bot.on_message(filters.command("stats"))
async def stats(client, message):
    users_count, groups_count = get_bot_stats()
    await message.reply(f"📊 Stats:\nUsers: {users_count}\nGroups: {groups_count}")
    log(f"/stats used by {message.from_user.id}")

@bot.on_message(filters.command("broadcast"))
async def broadcast(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("🚫 You are not authorized.")
    text = " ".join(message.command[1:])
    if not text:
        return await message.reply("❗ Provide a message.")
    log("Broadcast started.")
    count = 0
    try:
        async for dialog in bot.iter_dialogs():
            if dialog.chat.type in ("group", "supergroup"):
                await bot.send_message(dialog.chat.id, text)
                count += 1
    except Exception as e:
        error_log(f"Broadcast error: {e}")
    await message.reply(f"✅ Broadcasted to {count} groups.")

@bot.on_message(filters.text & ~filters.command)
async def spam_and_bio_scan(client, message):
    user = message.from_user
    text = message.text.lower()
    suspicious = any(keyword in text for keyword in ["http", "t.me", "@", "promo", "buy"])
    if suspicious:
        await message.delete()
        log_violation(user.id, "Spam/Bio Link Detected")
        log(f"⚠️ Spam deleted from {user.id}")
