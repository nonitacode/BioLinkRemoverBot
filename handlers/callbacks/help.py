from pyrogram import filters
from pyrogram.types import CallbackQuery
from bot.bot import app
from database.users import get_user_language
from utils.language import get_message
from utils.inline_buttons import commands_buttons

@app.on_callback_query(filters.regex("help_panel"))
async def help_panel_cb(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    lang = await get_user_language(user_id)
    help_text = get_message(lang, "help_message")

    await callback_query.message.edit_text(
        text=help_text,
        reply_markup=await commands_buttons(user_id)
    )
