from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from utils.language import get_message
from database.user_language import get_user_language
from utils.inline_buttons import commands_buttons, start_buttons, back_to_help_button

@app.on_callback_query(filters.regex("help_panel"))
async def help_panel_cb(client, query: CallbackQuery):
    user_id = query.from_user.id
    lang = get_user_language(user_id)
    help_text = get_message(lang, "help_message")

    await query.message.edit_text(
        text=help_text,
        reply_markup=await commands_buttons(user_id),
        disable_web_page_preview=True
    )

@app.on_callback_query(filters.regex("main_menu"))
async def back_to_main_menu(client, query: CallbackQuery):
    user_id = query.from_user.id
    lang = get_user_language(user_id)
    welcome_text = get_message(lang, "welcome_message")

    await query.message.edit_text(
        text=welcome_text,
        reply_markup=await start_buttons(user_id),
        disable_web_page_preview=True
    )

@app.on_callback_query(filters.regex("back_to_help"))
async def back_to_help(client, query: CallbackQuery):
    user_id = query.from_user.id
    lang = get_user_language(user_id)
    help_text = get_message(lang, "help_message")

    await query.message.edit_text(
        text=help_text,
        reply_markup=await commands_buttons(user_id),
        disable_web_page_preview=True
    )

@app.on_callback_query(filters.regex("help_allow"))
async def help_allow_cb(client, query):
    lang = get_user_language(query.from_user.id)
    msg = get_message(lang, "help_allow")
    await query.message.edit_text(msg, reply_markup=await back_to_help_button(query.from_user.id))

@app.on_callback_query(filters.regex("help_warn"))
async def help_warn_cb(client, query):
    lang = get_user_language(query.from_user.id)
    msg = get_message(lang, "help_warn")
    await query.message.edit_text(msg, reply_markup=await back_to_help_button(query.from_user.id))

@app.on_callback_query(filters.regex("help_mute"))
async def help_mute_cb(client, query):
    lang = get_user_language(query.from_user.id)
    msg = get_message(lang, "help_mute")
    await query.message.edit_text(msg, reply_markup=await back_to_help_button(query.from_user.id))

@app.on_callback_query(filters.regex("help_ban"))
async def help_ban_cb(client, query):
    lang = get_user_language(query.from_user.id)
    msg = get_message(lang, "help_ban")
    await query.message.edit_text(msg, reply_markup=await back_to_help_button(query.from_user.id))
