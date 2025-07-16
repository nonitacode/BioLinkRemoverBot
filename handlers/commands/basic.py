# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    await message.reply("✅ Pong! Bot is responsive.")

@bot.on_message(filters.command("alive"))
async def alive_command(client, message: Message):
    await message.reply("✅ I'm alive and working properly.")
