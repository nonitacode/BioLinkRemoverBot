from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import BOT_NAME

# /start command
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        f"Welcome to **{BOT_NAME}** – your smart bot for filtering bios and suspicious links in groups!\n\n"
        "**✨ Features:**\n"
        "• Detects spam/bio links & deletes automatically\n"
        "• Whitelist trusted users/groups\n"
        "• Admin-only tools for full control\n"
        "• Smart pattern recognition\n\n"
        "Click below to learn more ⬇️",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Help", callback_data="help_menu")],
            [
                InlineKeyboardButton("👨‍💻 Owner", callback_data="info_owner"),
                InlineKeyboardButton("🛠 Support", callback_data="info_support")
            ],
            [
                InlineKeyboardButton("📢 Updates", callback_data="info_updates"),
                InlineKeyboardButton("💻 Source Code", url="https://github.com/YourRepo/BioLinkScan")
            ]
        ])
    )


# Inline callback handler
async def callback_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "help_menu":
        await query.message.edit_text(
            "**📖 Help Menu - BioLinkScan**\n\n"
            "Click any option below to explore details:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧩 /start", callback_data="help_start")],
                [InlineKeyboardButton("📚 /help", callback_data="help_help")],
                [InlineKeyboardButton("📊 /stats", callback_data="help_stats")],
                [InlineKeyboardButton("✅ Whitelist Info", callback_data="help_whitelist")],
                [InlineKeyboardButton("🧠 How Bot Works", callback_data="help_how")],
                [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
            ])
        )

    elif data == "help_start":
        await query.message.edit_text(
            "**🧩 /start**\n\n"
            "Shows the welcome message with all buttons.",
            reply_markup=back_buttons()
        )

    elif data == "help_help":
        await query.message.edit_text(
            "**📚 /help**\n\n"
            "Lists all commands with usage details and features.",
            reply_markup=back_buttons()
        )

    elif data == "help_stats":
        await query.message.edit_text(
            "**📊 /stats or /about**\n\n"
            "Shows total groups & users using the bot.\nBot must be admin to view group stats.",
            reply_markup=back_buttons()
        )

    elif data == "help_whitelist":
        await query.message.edit_text(
            "**✅ Whitelist**\n\n"
            "Use `/whitelist` (admin-only) to mark safe users or groups.",
            reply_markup=back_buttons()
        )

    elif data == "help_how":
        await query.message.edit_text(
            "**🧠 How BioLinkScan Works**\n\n"
            "1. Monitors bios & messages\n"
            "2. Detects links or dangerous text\n"
            "3. Deletes & logs suspicious entries\n"
            "4. Mutes/bans after limit\n"
            "5. Skips whitelisted entries",
            reply_markup=back_buttons()
        )

    # Redirects for info buttons
    elif data == "info_owner":
        await query.message.reply_text("👨‍💻 **Bot Owner**\n\nContact: [@Nikchil](https://t.me/Nikchil)", disable_web_page_preview=True)

    elif data == "info_support":
        await query.message.reply_text("🛠 **Support Group**\n\nJoin: [@GrayBotSupport](https://t.me/GrayBotSupport)", disable_web_page_preview=True)

    elif data == "info_updates":
        await query.message.reply_text("📢 **Update Channel**\n\nSubscribe: [@GrayBots](https://t.me/GrayBots)", disable_web_page_preview=True)

    elif data == "start_menu":
        await start_handler(client, query.message)


# Reusable back button
def back_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Help", callback_data="help_menu")]
    ])
