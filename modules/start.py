# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from modules.inline import start_buttons
from bot.bot import bot
from config import BOT_NAME

@bot.on_message(filters.command("start"))
async def start(client, message):
    welcome_message = f"**Welcome to {BOT_NAME}!**\n\n" \
                      "Here you can interact with the bot, get stats, manage users, and more.\n" \
                      "Click the buttons below to get started!"
    keyboard = start_buttons()
    await message.reply(welcome_message, reply_markup=keyboard)
