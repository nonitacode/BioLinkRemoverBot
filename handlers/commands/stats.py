# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import bot
from database.users import get_users_count, get_groups_count

@bot.on_message(filters.command("stats"))
async def stats_command(client, message: Message):
    users = get_users_count()
    groups = get_groups_count()
    await message.reply(f"📊 **Bot Stats:**\n\n👤 Users: `{users}`\n👥 Groups: `{groups}`")
