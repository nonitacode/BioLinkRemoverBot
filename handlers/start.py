from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import BOT_NAME

async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        f"I am **{BOT_NAME}**, your smart link monitoring bot.\n"
        f"I can detect, delete and protect your groups from harmful or suspicious links.\n\n"
        f"Tap the button below for detailed help!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Help", callback_data="help_menu")]
        ])
    )

async def callback_handler(client: Client, query: CallbackQuery):
    if query.data == "help_menu":
        await query.message.edit_text(
            "**📖 Help Guide**\n\n"
            "🔹 Auto scans messages for links\n"
            "🔹 Deletes harmful or unapproved links\n"
            "🔹 Whitelist your users/groups\n"
            "🔹 Admin-only commands: /stats, /about\n"
            "🔹 Bio scanning support\n\n"
            "Use /help to get full command list.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
            ])
        )
    elif query.data == "start_menu":
        await query.message.edit_text(
            f"👋 Hello {query.from_user.mention}!\n\n"
            f"I am **{BOT_NAME}**, your smart link monitoring bot.\n"
            f"Tap below for help!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📖 Help", callback_data="help_menu")]
            ])
        )
