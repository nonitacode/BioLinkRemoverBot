# BioLinkRemoverBot - All rights reserved
# --------------------------------------
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from bot.bot import bot
from config import OWNER_ID
from database.violation_db import log_violation
from modules.inline import (
    start_buttons,
    commands_buttons,
    bot_commands_buttons,
    user_commands_buttons,
    moderation_commands_buttons,
    admin_commands_buttons
)

# Dummy placeholder functions (replace with your actual ones)
def store_user_data(user_id, username, full_name):
    pass

def get_bot_stats():
    return 1234, 567  # Replace with real stats

# ====== START COMMAND ======
@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    welcome_message = f"**Welcome to BioLinkRemoverBot!**\n\n" \
                      "You can manage your group, track spam, and more!\n" \
                      "Click the buttons below to get started!"
    await message.reply(welcome_message, reply_markup=start_buttons())

# ====== BOT COMMANDS ======
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

@bot.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("Welcome to the Help Panel. Choose a category to see the commands.", reply_markup=commands_buttons())

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

# ====== MODERATION COMMANDS ======
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

# ====== SPAM FILTERING ======
@bot.on_message(filters.text)
async def general_message(client, message):
    if message.text.startswith("/"):
        return

    text = message.text.lower()
    if any(keyword in text for keyword in ["http", "@", "promo", "buy", "sale"]):
        await message.delete()
        log_violation(message.from_user.id, "Spam detected")
        await message.reply("Your message has been deleted due to potential spam.")

# ====== CALLBACK QUERY HANDLERS ======

@bot.on_callback_query(filters.regex("about_me"))
async def about_me_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("**About BioLinkRemoverBot:**\nI help manage groups, auto-detect spam, warn/ban users, and more!")

@bot.on_callback_query(filters.regex("donate"))
async def donate_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Support the bot and keep it running!\nDonate via UPI: **itxnikhil@ptyes**")

@bot.on_callback_query(filters.regex("commands"))
async def command_categories(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Choose a category to view commands:", reply_markup=commands_buttons())

@bot.on_callback_query(filters.regex("bot_commands"))
async def bot_commands_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("These are the bot-related commands:", reply_markup=bot_commands_buttons())

@bot.on_callback_query(filters.regex("user_commands"))
async def user_commands_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("These are the user-related commands:", reply_markup=user_commands_buttons())

@bot.on_callback_query(filters.regex("moderation_commands"))
async def moderation_commands_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("These are the moderation commands:", reply_markup=moderation_commands_buttons())

@bot.on_callback_query(filters.regex("admin_commands"))
async def admin_commands_callback(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("These are the admin commands:", reply_markup=admin_commands_buttons())

# OPTIONAL - fallback unknown
@bot.on_callback_query()
async def unknown_callback(client, callback_query: CallbackQuery):
    await callback_query.answer("This button is not yet implemented!", show_alert=True)

# ====== RUN THE BOT ======
if __name__ == "__main__":
    print("Starting BioLinkRemoverBot...")
    bot.run()
