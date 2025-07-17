# Basic Callback Handlers

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from utils.language import get_message
from database.user_language import get_user_language
from utils.inline_buttons import start_buttons, commands_buttons

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

@app.on_callback_query(filters.regex("language_panel"))
async def language_panel_cb(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)
    await query.answer(get_message(lang, "choose_language"), show_alert=True)
