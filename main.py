# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from bot.bot import bot  # Importing the initialized bot object
from database.violation_db import log_violation
from config import OWNER_ID

# Define bot commands and their corresponding functions

@bot.on_message(filters.command("start"))
async def start(client, message):
    """Handles the /start command and stores user data"""
    user = message.from_user
    store_user_data(user.id, user.username, user.full_name)
    welcome_message = f"**Welcome to BioLinkRemoverBot!**\n\n" \
                      "You can manage your group, track spam, and more!\n" \
                      "Click below to get started!"
    keyboard = start_buttons()  # Inline buttons for starting
    await message.reply(welcome_message, reply_markup=keyboard)

@bot.on_message(filters.command("ping"))
async def ping(client, message):
    """Handles the /ping command and checks bot latency"""
    ping_time = "Ping successful!"
    await message.reply(ping_time)

@bot.on_message(filters.command("alive"))
async def alive(client, message):
    """Handles the /alive command and shows bot uptime"""
    alive_message = "I am alive and running smoothly!"
    await message.reply(alive_message)

@bot.on_message(filters.command("stats"))
async def stats(client, message):
    """Handles the /stats command and shows bot statistics"""
    users_count, groups_count = get_bot_stats()
    stats_message = f"Bot Statistics:\n\nUsers: {users_count}\nGroups: {groups_count}"
    await message.reply(stats_message)

@bot.on_message(filters.command("help"))
async def help(client, message):
    """Handles the /help command and shows help instructions"""
    help_message = "Use the following commands to interact with the bot:"
    help_message += "\n/start - Welcome message\n/ping - Check bot latency\n/alive - Check bot status"
    await message.reply(help_message)

@bot.on_message(filters.command("broadcast"))
async def broadcast(client, message):
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

@bot.on_message(filters.command("warn"))
async def warn_user(client, message):
    """Handles the /warn command and warns a user"""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User warned")
    await message.reply("User has been warned.")

@bot.on_message(filters.command("ban"))
async def ban_user(client, message):
    """Handles the /ban command and bans a user"""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User banned")
    await message.reply("User has been banned from the group.")

@bot.on_message(filters.command("mute"))
async def mute_user(client, message):
    """Handles the /mute command and mutes a user"""
    user_id = message.reply_to_message.from_user.id
    log_violation(user_id, "User muted")
    await message.reply("User has been muted.")

@bot.on_message(filters.text & ~filters.command())  # Correct filter to catch non-command text messages
async def general_message(client, message):
    """Handles general messages and checks for spam"""
    text = message.text.lower()
    if any(keyword in text for keyword in ["http", "@", "promo", "buy", "sale"]):
        await message.delete()  # Delete the message
        log_violation(message.from_user.id, "Spam detected")
        await message.reply("Your message has been deleted due to potential spam.")

# Run the bot by executing it
if __name__ == "__main__":
    log("Starting BioLinkRemoverBot...")
    bot.run()
