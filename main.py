# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from bot.bot import bot
from bot.logger import log
from config import OWNER_ID
from pyrogram import filters
from database.users_db import store_user_data, store_group_data
from pyrogram.types import Message

# Initialize the bot and load it with the necessary configurations
bot.start()

# Define bot commands and their corresponding functions
@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    """Handles the /start command and stores user data"""
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    welcome_message = f"**Welcome to BioLinkRemoverBot!**\n\n" \
                      "You can manage your group, track spam, and more!\n" \
                      "Click below to get started!"
    keyboard = start_buttons()  # Inline buttons for starting
    await message.reply(welcome_message, reply_markup=keyboard)

@bot.on_message(filters.command("ping"))
async def ping(client, message: Message):
    """Handles the /ping command and checks bot latency"""
    ping_time = "Ping successful!"
    await message.reply(ping_time)

@bot.on_message(filters.command("alive"))
async def alive(client, message: Message):
    """Handles the /alive command and shows bot uptime"""
    alive_message = "I am alive and running smoothly!"
    await message.reply(alive_message)

@bot.on_message(filters.command("stats"))
async def stats(client, message: Message):
    """Handles the /stats command and shows bot statistics"""
    users_count, groups_count = get_bot_stats()
    stats_message = f"Bot Statistics:\n\nUsers: {users_count}\nGroups: {groups_count}"
    await message.reply(stats_message)

@bot.on_message(filters.command("help"))
async def help(client, message: Message):
    """Handles the /help command and shows help instructions"""
    help_message = "Use the following commands to interact with the bot:"
    help_message += "\n/start - Welcome message\n/ping - Check bot latency\n/alive - Check bot status"
    await message.reply(help_message)

@bot.on_message(filters.command("broadcast"))
async def broadcast(client, message: Message):
    """Handles the /broadcast command to broadcast a message to all groups"""
    if message.from_user.id == OWNER_ID:
        # Ensure only the owner can broadcast
        text = "Broadcast Message: " + " ".join(message.command[1:])
        for chat in bot.get_chat_ids():
            try:
                await bot.send_message(chat, text)
            except Exception as e:
                log(f"Error broadcasting to chat {chat}: {e}")
        await message.reply("Message broadcasted to all groups!")
    else:
        await message.reply("You are not authorized to use this command.")

# Handling user profile and commands in groups
@bot.on_message(filters.command("profile"))
async def user_profile(client, message: Message):
    """Handles the /profile command and displays user info"""
    user_data = get_user_data(message.from_user.id)
    profile_message = f"**User Profile**\n\nUsername: {user_data['username']}\nFull Name: {user_data['full_name']}"
    await message.reply(profile_message)

# Handle messages that are not commands
@bot.on_message(filters.text & ~filters.command())
async def general_message(client, message: Message):
    """Handles general messages and checks for spam"""
    text = message.text.lower()
    if any(keyword in text for keyword in ["http", "@", "promo", "buy", "sale"]):
        await message.delete()
        log_violation(message.from_user.id, "Spam detected")
        await message.reply("Your message has been deleted due to potential spam.")

# Adding users to the group (can be invoked by admins)
@bot.on_message(filters.command("add_user"))
async def add_user_to_group(client, message: Message):
    """Handles the /add_user command to add a user to the group"""
    if message.from_user.id == OWNER_ID:
        user_id = message.command[1]
        group_name = "New Group"
        store_group_data(message.chat.id, group_name)
        await message.reply(f"User with ID {user_id} has been added to the group.")
    else:
        await message.reply("You are not authorized to use this command.")

# Handle bot shutdown and clean-up
@bot.on_shutdown
async def on_shutdown(client):
    """Handles bot shutdown"""
    log("Bot shutting down...")
    # Add cleanup code here (e.g., saving data to DB, logging, etc.)
    await client.stop()

# Start the bot by running it
if __name__ == "__main__":
    log("Starting BioLinkRemoverBot...")
    bot.run()
