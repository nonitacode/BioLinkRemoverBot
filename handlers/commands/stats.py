# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.users import get_users_count
from database.groups import get_groups_count

@app.on_message(filters.command("stats"))
async def stats_command(client, message: Message):
    users = await get_users_count()   # ✅ Await required
    groups = await get_groups_count() # ✅ Await required

    await message.reply(f"📊 **Bot Stats:**\n\n👤 Users: `{users}`\n👥 Groups: `{groups}`")
