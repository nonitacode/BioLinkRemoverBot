from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import BOT_NAME

# /start command
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        f"Welcome to **{BOT_NAME}** – Your ultimate anti-spam & suspicious link/bio filter bot for Telegram groups!\n\n"
        "**🛡 Key Features:**\n"
        "• Auto-detects harmful links & bio spam\n"
        "• Deletes malicious content automatically\n"
        "• Whitelist safe users/groups\n"
        "• Admin-only tools for managing violations\n"
        "• Smart filter with customizable actions\n\n"
        "Use the buttons below to get started ⬇️",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Help", callback_data="help_menu")],
            [
                InlineKeyboardButton("👨‍💻 Owner", url="https://t.me/Nikchil"),
                InlineKeyboardButton("🛠 Support", url="https://t.me/GrayBotSupport")
            ],
            [
                InlineKeyboardButton("📢 Updates", url="https://t.me/GrayBots"),
                InlineKeyboardButton("💻 GitHub", url="https://github.com/Nikchil/LinkScanBot")
            ]
        ])
    )


# Inline button callback navigation
async def callback_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "help_menu":
        await query.message.edit_text(
            "**📖 Help Menu - BioLinkScan**\n\n"
            "Click on a button below to learn about each command or feature:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧩 /start", callback_data="help_start")],
                [InlineKeyboardButton("📚 /help", callback_data="help_help")],
                [InlineKeyboardButton("📊 /stats", callback_data="help_stats")],
                [InlineKeyboardButton("✅ Whitelisting", callback_data="help_whitelist")],
                [InlineKeyboardButton("🧠 How Bot Works", callback_data="help_how")],
                [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
            ])
        )

    elif data == "help_start":
        await query.message.edit_text(
            "**🧩 /start**\n\n"
            "Displays welcome message, inline buttons, and general bot info.",
            reply_markup=back_buttons()
        )

    elif data == "help_help":
        await query.message.edit_text(
            "**📚 /help**\n\n"
            "Shows all commands, features, and usage instructions.",
            reply_markup=back_buttons()
        )

    elif data == "help_stats":
        await query.message.edit_text(
            "**📊 /stats or /about**\n\n"
            "Shows total groups linked and whitelisted users.\n"
            "Requires bot to be admin in the group.",
            reply_markup=back_buttons()
        )

    elif data == "help_whitelist":
        await query.message.edit_text(
            "**✅ Whitelisting**\n\n"
            "Use `/whitelist` to exclude trusted users or groups from link deletion.\n"
            "Only group admins can use this command.",
            reply_markup=back_buttons()
        )

    elif data == "help_how":
        await query.message.edit_text(
            "**🧠 How BioLinkScan Works**\n\n"
            "1. Monitors messages and bios for spam, links, and suspicious words.\n"
            "2. Matches against smart filters (`grabify`, short URLs, porn words, etc).\n"
            "3. Deletes and logs messages instantly.\n"
            "4. Mutes/bans after max violations.\n"
            "5. Fully skips trusted users and groups.",
            reply_markup=back_buttons()
        )

    elif data == "start_menu":
        await start_handler(client, query.message)


# Reusable back button
def back_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Help", callback_data="help_menu")]
    ])
