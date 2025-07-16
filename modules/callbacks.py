# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import CallbackQuery
from bot.bot import bot
from utils.language import get_message
from modules.inline import (
    start_buttons,
    commands_buttons,
    bot_commands_buttons,
    user_commands_buttons,
    moderation_commands_buttons,
    admin_commands_buttons,
    language_buttons,
)
from database.user_language_db import get_user_language, set_user_language

@bot.on_callback_query(filters.regex("about_me"))
async def about_callback(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "about_me")
    await query.message.edit_caption(caption=text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("donate"))
async def donate_callback(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "donate_info")
    await query.message.edit_caption(caption=text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("commands"))
async def command_category(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    title = get_message(lang, "commands_category")
    await query.message.edit_caption(caption=title, reply_markup=commands_buttons())

@bot.on_callback_query(filters.regex("bot_commands"))
async def bot_cmds(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "bot_commands")
    await query.message.edit_caption(caption=text, reply_markup=bot_commands_buttons())

@bot.on_callback_query(filters.regex("user_commands"))
async def user_cmds(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "user_commands")
    await query.message.edit_caption(caption=text, reply_markup=user_commands_buttons())

@bot.on_callback_query(filters.regex("moderation_commands"))
async def mod_cmds(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "moderation_commands")
    await query.message.edit_caption(caption=text, reply_markup=moderation_commands_buttons())

@bot.on_callback_query(filters.regex("admin_commands"))
async def admin_cmds(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "admin_commands")
    await query.message.edit_caption(caption=text, reply_markup=admin_commands_buttons())

@bot.on_callback_query(filters.regex("choose_lang"))
async def choose_lang_callback(client, query: CallbackQuery):
    await query.message.edit_caption("🌐 Please select your preferred language:", reply_markup=language_buttons())

@bot.on_callback_query(filters.regex("^lang_"))
async def set_lang(client, query: CallbackQuery):
    lang_code = query.data.split("_")[1]
    set_user_language(query.from_user.id, lang_code)
    text = get_message(lang_code, "welcome_message")
    await query.message.edit_caption(caption=text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("back_to_main"))
async def back_main(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    text = get_message(lang, "welcome_message")
    await query.message.edit_caption(caption=text, reply_markup=start_buttons())

@bot.on_callback_query(filters.regex("close_menu"))
async def close_menu(client, query: CallbackQuery):
    await query.message.delete()
