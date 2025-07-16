# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import time
from datetime import timedelta
from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from bot.helpers.lang import get_string  # adjust path if different

BOT_START_TIME = time.time()

def get_readable_time(seconds: int) -> str:
    return str(timedelta(seconds=int(seconds)))

@app.on_message(filters.command("ping") & (filters.chat_type.groups | filters.chat_type.private))
async def ping_command(client, message: Message):
    lang = await get_string(message.chat.id)
    
    start = time.time()
    sent = await message.reply(lang["basic"]["ping_reply_temp"])
    end = time.time()

    latency = round((end - start) * 1000, 3)
    uptime = get_readable_time(time.time() - BOT_START_TIME)

    await sent.edit_text(
        lang["basic"]["ping_final_reply"].format(
            uptime=uptime,
            latency=latency,
            ping=latency
        )
    )

@app.on_message(filters.command("alive") & (filters.chat_type.groups | filters.chat_type.private))
async def alive_command(client, message: Message):
    lang = await get_string(message.chat.id)
    
    start = time.time()
    sent = await message.reply(lang["basic"]["alive_reply_temp"])
    end = time.time()

    latency = round((end - start) * 1000, 3)
    uptime = get_readable_time(time.time() - BOT_START_TIME)

    await sent.edit_text(
        lang["basic"]["alive_final_reply"].format(
            uptime=uptime,
            latency=latency,
            ping=latency
        )
    )
