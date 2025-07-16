# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from utils.language import get_message
from utils.inline_buttons import commands_buttons, start_buttons

@Client.on_callback_query(filters.regex("help_menu"))
async def help_menu_cb(_, query: CallbackQuery):
    lang = "en"
    help_msg = get_message(lang, "help_message")
    await query.message.edit_caption(caption=help_msg, reply_markup=commands_buttons())

@Client.on_callback_query(filters.regex("main_menu"))
async def main_menu_cb(_, query: CallbackQuery):
    lang = "en"
    welcome = get_message(lang, "welcome_message")
    await query.message.edit_caption(caption=welcome, reply_markup=start_buttons())
