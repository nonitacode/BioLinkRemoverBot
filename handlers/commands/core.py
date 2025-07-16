# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from database.users import get_users_count
from database.groups import get_groups_count
from config import OWNER_ID

@Client.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply("✅ Pong!")

@Client.on_message(filters.command("alive"))
async def alive(_, message: Message):
    await message.reply("✅ Bot is alive and functioning.")

@Client.on_message(filters.command("stats"))
async def stats(_, message: Message):
    users = get_users_count()
    groups = get_groups_count()
    await message.reply(f"📊 **Bot Stats:**\n👤 Users: `{users}`\n👥 Groups: `{groups}`")
