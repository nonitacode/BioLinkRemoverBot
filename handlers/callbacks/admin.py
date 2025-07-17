# Admin Command Callback Handlers

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from utils.language import get_message
from database.user_language import get_user_language  # async function

@app.on_callback_query(filters.regex("help_allow"))
async def help_allow_cb(client, query: CallbackQuery):
    lang = await get_user_language(query.from_user.id)
    await query.message.edit_text(get_message(lang, "help_allow"))

@app.on_callback_query(filters.regex("help_mute"))
async def help_mute_cb(client, query: CallbackQuery):
    lang = await get_user_language(query.from_user.id)
    await query.message.edit_text(get_message(lang, "help_mute"))
