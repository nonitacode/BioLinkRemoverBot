# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID, BOT_NAME
from bot.bot import bot
from utils.language import get_message
from database.user_language_db import get_user_language
from database.users_db import store_user_data
from database.stats_db import get_bot_stats
from database.violation_db import log_violation
from utils.logger import log_to_channel
from modules.inline import start_buttons, commands_buttons

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    lang = get_user_language(user.id)
    welcome = get_message(lang, "welcome_message")
    photo = "assets/biolinkremoverbot.png"
    await log_to_channel(bot, f"🚀 {user.mention} started the bot.")
    await message.reply_photo(photo, caption=welcome, reply_markup=start_buttons())

@bot.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    lang = get_user_language(message.from_user.id)
    help_text = get_message(lang, "help_message")
    photo = "assets/biolinkremoverbot.png"
    await message.reply_photo(photo, caption=help_text, reply_markup=commands_buttons())

@bot.on_message(filters.command("ping"))
async def ping_handler(client, message: Message):
    await message.reply("✅ Pong!")

@bot.on_message(filters.command("alive"))
async def alive_handler(client, message: Message):
    await message.reply("✅ I'm alive and working perfectly.")

@bot.on_message(filters.command("stats"))
async def stats_handler(client, message: Message):
    users, groups = get_bot_stats()
    await message.reply(f"📊 Bot Stats:\n👤 Users: {users}\n👥 Groups: {groups}")

@bot.on_message(filters.command("warn"))
async def warn_user(client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        log_violation(user_id, "User warned")
        await message.reply("⚠️ User has been warned.")

@bot.on_message(filters.command("ban"))
async def ban_user(client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        log_violation(user_id, "User banned")
        await message.reply("🚫 User has been banned.")

@bot.on_message(filters.command("mute"))
async def mute_user(client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        log_violation(user_id, "User muted")
        await message.reply("🔇 User has been muted.")

@bot.on_message(filters.text)
async def bio_link_detector(client, message: Message):
    if message.text.startswith("/"):
        return
    text = message.text.lower()
    if any(x in text for x in ["http", "@", "t.me", "link", "promo", "sale", "buy"]):
        await message.delete()
        log_violation(message.from_user.id, "Detected spam or promotional link")
        await log_to_channel(bot, f"🚫 Deleted spam message from [{message.from_user.id}](tg://user?id={message.from_user.id})")
