async def start_buttons(user_id: int, lang_code: str = None):
    lang_code = lang_code or await get_user_language(user_id)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_message(lang_code, "ADD"), url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton(get_message(lang_code, "DEVELOPER"), url="https://t.me/nikchil"),
            InlineKeyboardButton(get_message(lang_code, "HELP_MENU"), callback_data="help_panel")
        ],
        [
            InlineKeyboardButton(get_message(lang_code, "SUPPORT"), url=SUPPORT_GROUP),
            InlineKeyboardButton(get_message(lang_code, "UPDATES"), url=UPDATES_CHANNEL)
        ],
        [InlineKeyboardButton(get_message(lang_code, "LANGUAGE"), callback_data="language_panel")]
    ])

async def commands_buttons(user_id: int, lang_code: str = None):
    lang_code = lang_code or await get_user_language(user_id)
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(get_message(lang_code, "ALLOW_CMD"), callback_data="help_allow"),
            InlineKeyboardButton(get_message(lang_code, "WARN_CMD"), callback_data="help_warn")
        ],
        [
            InlineKeyboardButton(get_message(lang_code, "MUTE_CMD"), callback_data="help_mute"),
            InlineKeyboardButton(get_message(lang_code, "BAN_CMD"), callback_data="help_ban")
        ],
        [InlineKeyboardButton(get_message(lang_code, "BACK"), callback_data="main_menu")]
    ])

async def back_to_help_button(user_id: int, lang_code: str = None):
    lang_code = lang_code or await get_user_language(user_id)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_message(lang_code, "BACK"), callback_data="help_panel")]
    ])
