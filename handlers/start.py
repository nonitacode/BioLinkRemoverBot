from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import BOT_NAME
import asyncio

# /start command
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        f"Welcome to **{BOT_NAME}** – Telegram's smart bio/link protection bot!\n\n"
        "**✨ Features:**\n"
        "• Filters harmful bios & links\n"
        "• Whitelist trusted users/groups\n"
        "• Admin-only tools, logging & stats\n\n"
        "Use the buttons below to explore 👇",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Help", callback_data="help_menu")],
            [
                InlineKeyboardButton("👨‍💻 Owner", callback_data="open_owner"),
                InlineKeyboardButton("🛠 Support", callback_data="open_support")
            ],
            [
                InlineKeyboardButton("📢 Updates", callback_data="open_updates"),
                InlineKeyboardButton("💻 Source Code", url="https://github.com/Nikchil/LinkScanBot")
            ]
        ])
    )


# Callback Handler
async def callback_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "help_menu":
        await query.message.edit_text(
            "**📖 Help Menu - BioLinkScan**\n\n"
            "Choose a feature to learn more:",
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
        await query.message.edit_text("**🧩 /start**\n\nShows welcome message and buttons.", reply_markup=back_buttons())

    elif data == "help_help":
        await query.message.edit_text("**📚 /help**\n\nLists all commands and usage.", reply_markup=back_buttons())

    elif data == "help_stats":
        await query.message.edit_text("**📊 /stats**\n\nShows total users/groups.", reply_markup=back_buttons())

    elif data == "help_whitelist":
        await query.message.edit_text("**✅ Whitelist Info**\n\nExclude trusted users/groups from filters.", reply_markup=back_buttons())

    elif data == "help_how":
        await query.message.edit_text("**🧠 How It Works**\n\nScans bios/messages, deletes links, bans violators.", reply_markup=back_buttons())

    elif data == "start_menu":
        await start_handler(client, query.message)

    # 🔁 Redirect-style replies (cleanest possible)
    elif data == "open_owner":
        msg = await query.message.reply_text("👨‍💻 [Click here to contact Owner](https://t.me/Nikchil)", disable_web_page_preview=True)
        await asyncio.sleep(5)
        await msg.delete()

    elif data == "open_support":
        msg = await query.message.reply_text("🛠 [Join Support Group](https://t.me/GrayBotSupport)", disable_web_page_preview=True)
        await asyncio.sleep(5)
        await msg.delete()

    elif data == "open_updates":
        msg = await query.message.reply_text("📢 [Subscribe to Updates](https://t.me/GrayBots)", disable_web_page_preview=True)
        await asyncio.sleep(5)
        await msg.delete()


# Reusable back button
def back_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Help", callback_data="help_menu")]
    ])
