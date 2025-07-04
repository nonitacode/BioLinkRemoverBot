from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters

BOT_USERNAME = "BioLinkRemoverBot"
SUPPORT_GROUP = "https://t.me/GrayBotSupport"
UPDATES_CHANNEL = "https://t.me/GrayBots"
DEVELOPER = "https://t.me/Nikchil"

def init(app):
    # /help command handler (NEWLY ADDED)
    @app.on_message(filters.command("help"))
    async def help_command(_, message: Message):
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Basics", callback_data="help_basic"),
                InlineKeyboardButton("Broadcast", callback_data="help_broadcast")
            ],
            [
                InlineKeyboardButton("Config", callback_data="help_config"),
                InlineKeyboardButton("Moderation", callback_data="help_moderation")
            ],
            [
                InlineKeyboardButton("Sudo Commands", callback_data="help_sudo"),
                InlineKeyboardButton("Utilities", callback_data="help_util")
            ],
            [
                InlineKeyboardButton("⬅️ Back", callback_data="back_home")
            ]
        ])
        await message.reply(
            """
<b>🛠️ Help Center — Choose a Section</b>

• Basics – Getting started & ping  
• Broadcast – Send messages to all users/groups  
• Config – Group settings & punishment rules  
• Moderation – Scan usernames/bios for links  
• Sudo – Owner-only tools  
• Utilities – Admin, whitelist, refresh tools
            """,
            reply_markup=keyboard
        )

    @app.on_callback_query(filters.regex("show_help"))
    async def show_help_menu(_, cb: CallbackQuery):
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Basics", callback_data="help_basic"),
                InlineKeyboardButton("Broadcast", callback_data="help_broadcast")
            ],
            [
                InlineKeyboardButton("Config", callback_data="help_config"),
                InlineKeyboardButton("Moderation", callback_data="help_moderation")
            ],
            [
                InlineKeyboardButton("Sudo Commands", callback_data="help_sudo"),
                InlineKeyboardButton("Utilities", callback_data="help_util")
            ],
            [
                InlineKeyboardButton("⬅️ Back", callback_data="back_home")
            ]
        ])

        await cb.message.edit_text(
            """
<b>🛠️ Help Center — Choose a Section</b>

• Basics – Getting started & ping  
• Broadcast – Send messages to all users/groups  
• Config – Group settings & punishment rules  
• Moderation – Scan usernames/bios for links  
• Sudo – Owner-only tools  
• Utilities – Admin, whitelist, refresh tools
            """,
            reply_markup=keyboard
        )

    @app.on_callback_query(filters.regex("help_basic"))
    async def help_basic(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>📌 Basic Commands</b>

/start — Welcome message and intro  
/help — Show help menu  
/ping — Check latency & uptime  
/biolink enable|disable — Toggle bio scanner in your group
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_broadcast"))
    async def help_broadcast(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>📣 Broadcast System</b>

/broadcast -all — Send to all users & groups  
/broadcast -user — Send to user chats only  
/broadcast -group — Send to group chats only  
Add <i>-forward</i> to forward instead of copy
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_config"))
    async def help_config(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>⚙️ Config Panel</b>

/config — Launch inline group settings  
• Set warn limit  
• Choose punishment (mute/ban)  
• Toggle bio scanning
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_moderation"))
    async def help_moderation(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>🚫 Moderation System</b>

Triggers on:
• Usernames, bios with links  
• Spam words or unwanted domains

Action Path:
⚠️ Warn → 🔇 Mute → 🔒 Ban
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_sudo"))
    async def help_sudo(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>👑 Sudo-Only Commands</b>

/broadcast -all | -user | -group  
/refresh — Reload config cache  
/admincache — Refresh group admin list
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_util"))
    async def help_util(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>🧰 Utility Commands</b>

/allow — Add a user to whitelist  
/remove — Remove from whitelist  
/freelist — List all whitelisted users  
/refresh — Sync memory and DB  
/admincache — Refresh admin list
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("back_home"))
    async def go_back_to_start(_, cb: CallbackQuery):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("Developer", url=DEVELOPER),
                InlineKeyboardButton("Help Menu", callback_data="show_help")
            ],
            [
                InlineKeyboardButton("Support", url=SUPPORT_GROUP),
                InlineKeyboardButton("Updates", url=UPDATES_CHANNEL)
            ]
        ])

        await cb.message.edit_text(
            f"""
👋 <b>Welcome to <u>Bio Link Remover Bot</u>!</b>

🛡️ <b>Cleaner Groups, Safer Chats</b>
• Detect and act on spam bios/usernames
• Tools for admins and auto moderation

<i>Use the buttons below to begin 👇</i>
            """,
            reply_markup=keyboard
        )
