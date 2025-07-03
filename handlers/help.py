from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters

BOT_USERNAME = "BioLinkRemoverBot"
SUPPORT_GROUP = "https://t.me/GrayBotSupport"
UPDATES_CHANNEL = "https://t.me/GrayBots"
DEVELOPER = "https://t.me/Nikchil"

def init(app):
    @app.on_callback_query(filters.regex("show_help"))
    async def show_help_menu(_, cb: CallbackQuery):
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⚙️ Config", callback_data="help_config"),
                InlineKeyboardButton("🚫 Moderation", callback_data="help_moderation")
            ],
            [
                InlineKeyboardButton("📣 Broadcast", callback_data="help_broadcast"),
                InlineKeyboardButton("🧰 Utilities", callback_data="help_util")
            ],
            [
                InlineKeyboardButton("👑 Sudo Commands", callback_data="help_sudo"),
                InlineKeyboardButton("📌 Basics", callback_data="help_basic")
            ],
            [
                InlineKeyboardButton("⬅️ Back", callback_data="back_home")
            ]
        ])

        await cb.message.edit_text(
            """
<b>🛠️ Help Panel — Choose a Category</b>

Select the type of commands you want help with:

⚙️ Config – Customize group behavior  
🚫 Moderation – Scan usernames, bio & messages  
📣 Broadcast – Mass send messages to groups/users  
🧰 Utilities – Ping, whitelist, refresh  
👑 Sudo – Owner-only bot controls  
📌 Basics – Starting and using the bot
            """,
            reply_markup=keyboard
        )

    @app.on_callback_query(filters.regex("help_basic"))
    async def help_basic(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>📌 Basic Commands</b>

<b>/start</b> — Show welcome panel & features  
<b>/help</b> — Show help categories panel  
<b>/ping</b> — Check real-time latency & uptime

These work in both private chat & groups.
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

<b>/broadcast -all</b> — Send message to all groups & users  
<b>/broadcast -user</b> — Send only to users  
<b>/broadcast -group</b> — Send only to groups  

<b>/refresh</b> — Reload memory & Mongo cache  
<b>/admincache</b> — Reload admin list for all groups  

<i>These are limited to OWNER_ID or sudoers only.</i>
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_config"))
    async def help_config(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>⚙️ Group Configuration Commands</b>

<b>/config</b> — Opens group config panel with inline buttons  
Set warn limit, choose punishment (mute/ban), and more — all from a sleek inline menu.

<i>Only available in groups where bot is admin.</i>
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

<b>🔗 Auto Triggered On:</b>  
• Any message containing links or @usernames  
• User bios with Telegram usernames, links, or spam words

<b>🔨 Action Flow:</b>  
1. ⚠️ First warn with reason  
2. 🔇 Mute after limit  
3. 🔒 Ban (if configured)

Admins will see inline buttons for unmute and whitelist when available.
            """,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Back", callback_data="show_help")]
            ])
        )

    @app.on_callback_query(filters.regex("help_broadcast"))
    async def help_broadcast(_, cb: CallbackQuery):
        await cb.message.edit_text(
            """
<b>📣 Broadcast Commands</b>

<b>/broadcast -all</b> — Send message to all groups & users  
<b>/broadcast -user</b> — To personal chats only  
<b>/broadcast -group</b> — To groups only

Use -forward to forward instead of copying.

<i>Example:</i>  
<code>/broadcast -all -forward</code>
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

<b>/allow</b> — Whitelist a user to bypass filters  
<b>/remove</b> — Remove from whitelist  
<b>/freelist</b> — Show all allowed users

<b>/refresh</b> — Reload Mongo/memory configs  
<b>/admincache</b> — Update group admin list
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
                InlineKeyboardButton("🛠 Help", callback_data="show_help"),
                InlineKeyboardButton("👨‍💻 Developer", url=DEVELOPER)
            ],
            [
                InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL),
                InlineKeyboardButton("🆘 Support", url=SUPPORT_GROUP)
            ]
        ])

        await cb.message.edit_text(
            f"""
👋 <b>Welcome to Bio Link Remover Bot!</b> 🛡️

<b>I protect your groups from:</b>  
• Unwanted links in bios and messages  
• Spam users with external URLs

<b>🔧 Features:</b>  
• Auto-link removal in chat  
• Bio link scans  
• Custom warnings, mute/ban  
• Whitelist trusted users

➕ <b>Add me to your group to activate protection.</b>  
🤖 <i>Powered by</i> <a href="{UPDATES_CHANNEL}">@GrayBots</a>
            """,
            reply_markup=keyboard
        )
