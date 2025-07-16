from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from bot.bot import bot
from config import OWNER_ID
from database.violation_db import log_violation
from database.user_language_db import get_user_language
from utils.language import get_message
from modules.inline import (
    start_buttons,
    commands_buttons,
    bot_commands_buttons,
    user_commands_buttons,
    moderation_commands_buttons,
    admin_commands_buttons,
    language_buttons
)
from database.users_db import store_user_data, get_bot_stats

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
    await message.reply("Ping successful!")

@bot.on_message(filters.command("alive"))
async def alive(client, message):
    await message.reply("I am alive and running smoothly!")

@bot.on_message(filters.command("stats"))
async def stats(client, message):
    users_count, groups_count = get_bot_stats()
    await message.reply(f"Bot Statistics:\n\nUsers: {users_count}\nGroups: {groups_count}")

@bot.on_message(filters.command("broadcast"))
async def broadcast(client, message):
    if message.from_user.id == OWNER_ID:
        text = "Broadcast Message: " + " ".join(message.command[1:])
        for chat in bot.get_chat_ids():
            try:
                await bot.send_message(chat, text)
            except Exception as e:
                print(f"Error broadcasting to chat {chat}: {e}")
        await message.reply("Message broadcasted to all groups!")
    else:
        await message.reply("You are not authorized to use this command.")

@bot.on_message(filters.command("warn"))
async def warn_user(client, message):
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User warned")
    await message.reply("User has been warned.")

@bot.on_message(filters.command("ban"))
async def ban_user(client, message):
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User banned")
    await message.reply("User has been banned from the group.")

@bot.on_message(filters.command("mute"))
async def mute_user(client, message):
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User muted")
    await message.reply("User has been muted.")

@bot.on_message(filters.text)
async def general_message(client, message):
    if message.text.startswith("/"):
        return
    text = message.text.lower()
    if any(keyword in text for keyword in ["http", "@", "promo", "buy", "sale"]):
        await message.delete()
        log_violation(message.from_user.id, "Spam detected")
        await message.reply("Your message has been deleted due to potential spam.")
