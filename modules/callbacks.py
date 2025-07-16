# BioLinkRemoverBot - Callback Query Handlers
# --------------------------------------------
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from bot.bot import bot
from modules.inline import (
    commands_buttons,
    bot_commands_buttons,
    user_commands_buttons,
    moderation_commands_buttons,
    admin_commands_buttons
)

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

@bot.on_callback_query()
async def unknown_callback(client, callback_query: CallbackQuery):
    await callback_query.answer("This button is not yet implemented!", show_alert=True)
