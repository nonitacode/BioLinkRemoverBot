# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from modules.inline import user_commands_buttons  # Import the inline buttons
from config import OWNER_ID
from bot.bot import bot

# Handle user commands callback queries
@bot.on_message(filters.command("user_commands"))
async def user_commands(client, message):
    """Handles the /user_commands command"""
    # Send a message with inline buttons for user commands
    keyboard = user_commands_buttons()  # Using the buttons from the inline.py module
    await message.reply("These are the user-related commands:", reply_markup=keyboard)

# Handle callback queries from user commands
@bot.on_callback_query(filters.regex("addauth"))
async def addauth_callback(client, callback_query):
    """Handle the 'Add to Whitelist' button click"""
    await callback_query.answer("Adding user to the whitelist...")
    user_id = callback_query.from_user.id
    # Logic to add user to whitelist (example: save to DB)
    await callback_query.message.edit_text("User added to the whitelist!")

@bot.on_callback_query(filters.regex("removeauth"))
async def removeauth_callback(client, callback_query):
    """Handle the 'Remove from Whitelist' button click"""
    await callback_query.answer("Removing user from the whitelist...")
    user_id = callback_query.from_user.id
    # Logic to remove user from whitelist (example: remove from DB)
    await callback_query.message.edit_text("User removed from the whitelist!")

@bot.on_callback_query(filters.regex("warn"))
async def warn_callback(client, callback_query):
    """Handle the 'Warn User' button click"""
    await callback_query.answer("Warning the user...")
    user_id = callback_query.from_user.id
    # Logic to warn the user (example: log warning)
    await callback_query.message.edit_text("User has been warned.")

@bot.on_callback_query(filters.regex("profile"))
async def profile_callback(client, callback_query):
    """Handle the 'Show Profile' button click"""
    await callback_query.answer("Showing profile...")
    user_id = callback_query.from_user.id
    # Logic to fetch and show user profile
    await callback_query.message.edit_text(f"Showing profile for user: {user_id}")
