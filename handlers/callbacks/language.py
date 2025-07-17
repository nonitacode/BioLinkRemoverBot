# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from database.user_language import set_user_language, get_user_language
from utils.language import get_message
from utils.inline_buttons import start_buttons
from config import START_IMG

@app.on_callback_query(filters.regex("language_panel"))
async def language_panel_cb(client, query: CallbackQuery):
    lang = get_user_language(query.from_user.id)

    text = get_message(lang, "choose_language") or "🌐 **Select your language**\n\nChoose the language you prefer."

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en"),
            InlineKeyboardButton("🇮🇳 Hindi", callback_data="set_lang_hi")
        ],
        [InlineKeyboardButton(get_message(lang, "back_button") or "🔙 Back", callback_data="main_menu")]
    ])

    await query.message.edit_text(text, reply_markup=buttons)

@app.on_callback_query(filters.regex("set_lang_(.*)"))
async def set_language(client, query: CallbackQuery):
    lang_code = query.data.split("_")[-1]
    user_id = query.from_user.id

    # Save user language to DB
    set_user_language(user_id, lang_code)

    # Confirmation popup
    confirmation = f"✅ Language set to `{lang_code}`."
    await query.answer(confirmation, show_alert=True)

    # Reload updated language
    welcome = get_message(lang_code, "welcome_message").format(user=query.from_user.mention)

    try:
        await query.message.edit_media(
            media=InputMediaPhoto(media=START_IMG, caption=welcome),
            reply_markup=await start_buttons(user_id)
        )
    except:
        await query.message.edit_text(
            text=welcome,
            reply_markup=await start_buttons(user_id)
        )
