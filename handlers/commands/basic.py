# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import time
from datetime import timedelta
from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from utils.language import get_message  # ✅ Corrected import

BOT_START_TIME = time.time()

def get_readable_time(seconds: int) -> str:
    return str(timedelta(seconds=int(seconds)))

@app.on_message(filters.command("ping") & ~filters.channel)
async def ping_command(client, message: Message):
    lang = "en"  # Later you can load dynamically per chat
    reply_temp = get_message(lang, "PING")
    reply_final = get_message(lang, "PING_FINAL")

    start = time.time()
    sent = await message.reply(reply_temp)
    end = time.time()

    ping = round((end - start) * 1000, 3)
    uptime = get_readable_time(time.time() - BOT_START_TIME)

    await sent.edit_text(
        reply_final.format(
            uptime=uptime,
            ping=latency
        )
    )

@app.on_message(filters.command("alive") & ~filters.channel)
async def alive_command(client, message: Message):
    lang = "en"
    reply_temp = get_message(lang, "ALIVE")
    reply_final = get_message(lang, "ALIVE_FINAL")

    start = time.time()
    sent = await message.reply(reply_temp)
    end = time.time()

    ping = round((end - start) * 1000, 3)
    uptime = get_readable_time(time.time() - BOT_START_TIME)

    await sent.edit_text(
        reply_final.format(
            uptime=uptime,
            ping=latency
        )
    )
