# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from utils.language import get_message
from database.user_language import get_user_language
from utils.inline_buttons import commands_buttons

@app.on_callback_query(filters.regex("help_panel"))
async def help_panel_cb(client, query: CallbackQuery):
    user_id = query.from_user.id
    lang = get_user_language(user_id)
    help_text = get_message(lang, "HELP")

    await query.message.edit_text(
        text=help_text,
        reply_markup=commands_buttons(user_id),  # ✅ Pass user_id here
        disable_web_page_preview=True
    )
