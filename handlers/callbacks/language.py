from bot.bot import app
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from database.user_language import set_user_language, get_user_language
from utils.language import get_message
from utils.inline_buttons import start_buttons
from config import START_IMG

@app.on_callback_query(filters.regex("language_panel"))
async def language_panel_cb(client, query: CallbackQuery):
    lang = await get_user_language(query.from_user.id)  # ✅ await here

    text = get_message(lang, "choose_language") or "🌐 **Select your language**\n\nChoose the language you prefer."

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en"),
            InlineKeyboardButton("🇮🇳 Hindi", callback_data="set_lang_hi")
        ],
        [
            InlineKeyboardButton("🇪🇸 Español", callback_data="set_lang_es"),
            InlineKeyboardButton("🇵🇹 Português", callback_data="set_lang_pt")
        ],
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="set_lang_ru"),
            InlineKeyboardButton("🇸🇦 العربية", callback_data="set_lang_ar")
        ],
        [InlineKeyboardButton(get_message(lang, "BACK") or "🔙 Back", callback_data="main_menu")]
    ])

    await query.message.edit_text(text, reply_markup=buttons)


@app.on_callback_query(filters.regex("set_lang_(.*)"))
async def set_language(client, query: CallbackQuery):
    lang_code = query.data.split("_")[-1]
    user_id = query.from_user.id

    # Save the new language to DB
    await set_user_language(user_id, lang_code)

    # Instant user feedback
    await query.answer(f"✅ Language set to `{lang_code}`.", show_alert=True)

    # Load message in selected language
    welcome = get_message(lang_code, "welcome_message").format(user=query.from_user.mention)

    try:
        await query.message.edit_media(
            media=InputMediaPhoto(media=START_IMG, caption=welcome),
            reply_markup=await start_buttons(user_id, lang_code=lang_code)  # ✅ Pass lang directly
        )
    except:
        await query.message.edit_text(
            text=welcome,
            reply_markup=await start_buttons(user_id, lang_code=lang_code)  # ✅ Pass lang directly
        )
