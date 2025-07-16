from pyrogram import Client, filters
from modules.inline import user_commands_buttons
from config import OWNER_ID
from bot.bot import bot

@bot.on_message(filters.command("user_commands"))
async def user_commands(client, message):
    """Handles the /user_commands command"""
    keyboard = user_commands_buttons()
    await message.reply(language_data["user_commands"], reply_markup=keyboard)

@bot.on_callback_query(filters.regex("addauth"))
async def addauth_callback(client, callback_query):
    """Handle the 'Add to Whitelist' button click"""
    await callback_query.answer("Adding user to the whitelist...")
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text("User added to the whitelist!")

@bot.on_callback_query(filters.regex("removeauth"))
async def removeauth_callback(client, callback_query):
    """Handle the 'Remove from Whitelist' button click"""
    await callback_query.answer("Removing user from the whitelist...")
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text("User removed from the whitelist!")

@bot.on_callback_query(filters.regex("warn"))
async def warn_callback(client, callback_query):
    """Handle the 'Warn User' button click"""
    await callback_query.answer("Warning the user...")
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text("User has been warned.")

@bot.on_callback_query(filters.regex("profile"))
async def profile_callback(client, callback_query):
    """Handle the 'Show Profile' button click"""
    await callback_query.answer("Showing profile...")
    user_id = callback_query.from_user.id
    await callback_query.message.edit_text(f"Showing profile for user: {user_id}")
