# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app

@app.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    await message.reply("✅ Pong! Bot is responsive.")

@app.on_message(filters.command("alive"))
async def alive_command(client, message: Message):
    await message.reply("✅ I'm alive and working properly.")
