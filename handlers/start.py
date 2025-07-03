from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@filters.command("start")
def start_command(client, message: Message):
    user = message.from_user.first_name
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠 Help & Commands", callback_data="show_help")]
    ])
    message.reply_text(
        f"👋 Hello {user}!\n\nI'm your anti-spam guardian bot 🛡️\n\nI can:\n• Auto-delete links & usernames\n• Scan bios for threats\n• Auto-mute spammers\n• Whitelist trusted members\n• Broadcast to users/groups\n\nUse the button below to explore all features.👇",
        reply_markup=keyboard
    )

@client.on_callback_query(filters.regex("show_help"))
def handle_start_help(client, callback):
    from handlers.help import help_command_buttons
    callback.message.edit(
        "🛠 Choose a command to view help:",
        reply_markup=help_command_buttons()
    )
