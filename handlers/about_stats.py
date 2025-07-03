from pyrogram import filters
from pyrogram.types import Message
from database.mongo import users, chats

@filters.command("about")
def about_handler(client, message: Message):
    message.reply_text(
        "🤖 *LinkScanBot*\n\nBuilt to secure your group from unwanted spam, links, and usernames.\n\nFeatures:\n• Auto-link deletion\n• Bio scan on joins\n• Auto-mute repeat offenders\n• Whitelist system\n• Broadcast to users/groups\n• Admin-only control",
        parse_mode="markdown"
    )

@filters.command("stats")
def stats_handler(client, message: Message):
    total_users = users.count_documents({})
    total_groups = chats.count_documents({})
    message.reply_text(
        f"📊 *Stats*\n\n👤 Users: {total_users}\n👥 Groups: {total_groups}",
        parse_mode="markdown"
    )
