# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from modules.inline import commands_buttons
from bot.bot import bot

@bot.on_message(filters.command("help"))
async def help(client, message):
    help_message = "Welcome to the Help Panel. Choose a category to see the commands."
    keyboard = commands_buttons()
    await message.reply(help_message, reply_markup=keyboard)
