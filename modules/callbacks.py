from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from bot.bot import bot
from modules.inline import (
    start_buttons,
    commands_buttons,
    bot_commands_buttons,
    user_commands_buttons,
    moderation_commands_buttons,
    admin_commands_buttons,
    language_buttons
)
from database.language_db import get_user_language, set_user_language
from utils.language import get_message

@bot.on_callback_query(filters.regex("about_me"))
async def about_me_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    about_text = get_message(lang, "about_me")
    await callback_query.answer()
    await callback_query.message.edit_text(about_text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("donate"))
async def donate_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    donate_text = get_message(lang, "donate_info")
    await callback_query.answer()
    await callback_query.message.edit_text(donate_text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("commands"))
async def command_categories(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    title = get_message(lang, "commands_category")
    await callback_query.answer()
    await callback_query.message.edit_text(title, reply_markup=commands_buttons())

@bot.on_callback_query(filters.regex("bot_commands"))
async def bot_commands_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    msg = get_message(lang, "bot_commands")
    await callback_query.answer()
    await callback_query.message.edit_text(msg, reply_markup=bot_commands_buttons())

@bot.on_callback_query(filters.regex("user_commands"))
async def user_commands_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    msg = get_message(lang, "user_commands")
    await callback_query.answer()
    await callback_query.message.edit_text(msg, reply_markup=user_commands_buttons())

@bot.on_callback_query(filters.regex("moderation_commands"))
async def moderation_commands_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    msg = get_message(lang, "moderation_commands")
    await callback_query.answer()
    await callback_query.message.edit_text(msg, reply_markup=moderation_commands_buttons())

@bot.on_callback_query(filters.regex("admin_commands"))
async def admin_commands_callback(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    msg = get_message(lang, "admin_commands")
    await callback_query.answer()
    await callback_query.message.edit_text(msg, reply_markup=admin_commands_buttons())

@bot.on_callback_query(filters.regex("choose_lang"))
async def choose_language(client, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Please select your preferred language:", reply_markup=language_buttons())

@bot.on_callback_query(filters.regex("^lang_"))
async def set_language(client, callback_query: CallbackQuery):
    lang_code = callback_query.data.split("_")[1]
    set_user_language(callback_query.from_user.id, lang_code)
    msg = get_message(lang_code, "welcome_message")
    await callback_query.answer("Language updated!")
    await callback_query.message.edit_text(msg, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("back_to_main"))
async def back_to_main(client, callback_query: CallbackQuery):
    lang = get_user_language(callback_query.from_user.id)
    msg = get_message(lang, "welcome_message")
    await callback_query.answer()
    await callback_query.message.edit_text(msg, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("close_menu"))
async def close_menu(client, callback_query: CallbackQuery):
    await callback_query.answer("Closed", show_alert=False)
    await callback_query.message.delete()

@bot.on_callback_query()
async def unknown_callback(client, callback_query: CallbackQuery):
    await callback_query.answer("This button is not yet implemented!", show_alert=True)
