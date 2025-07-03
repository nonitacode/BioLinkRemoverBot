from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@filters.command("help")
def help_command(client, message: Message):
    keyboard = help_command_buttons()
    message.reply("🛠 Choose a command to view help:", reply_markup=keyboard)

@client.on_callback_query()
def help_callback(client, callback):
    data = callback.data
    help_texts = {
        "help_links": "🔗 *Anti-Link System*\nAutomatically deletes messages with links or @usernames.\nAlso scans new users' bios.\nRepeat offenders get muted.",
        "help_whitelist": "👤 *Whitelist*\nReply to a user:\n`/whitelist` – Allow links\n`/unwhitelist` – Remove access",
        "help_settings": "⚙ *Settings*\n`/settings on` – Enable scan\n`/settings off` – Disable scan",
        "help_broadcast": "📢 *Broadcast*\nReply to any message:\n`/broadcast -all` – All users/groups\n`/broadcast -group` – Groups only\n`/broadcast -user` – Private users only"
    }

    if data in help_texts:
        callback.answer()
        callback.message.edit(help_texts[data], parse_mode="Markdown", reply_markup=help_command_buttons())

def help_command_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Anti-Link", callback_data="help_links"),
         InlineKeyboardButton("👤 Whitelist", callback_data="help_whitelist")],
        [InlineKeyboardButton("⚙ Settings", callback_data="help_settings"),
         InlineKeyboardButton("📢 Broadcast", callback_data="help_broadcast")]
    ])
