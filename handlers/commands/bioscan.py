# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from database.bioscan_db import set_bioscan_status, get_bioscan_status
from utils.language import get_message
from database.user_language import get_user_language

@app.on_message(filters.command("bioscan") & filters.group)
async def bioscan_toggle(client, message: Message):
    lang = await get_user_language(message.from_user.id)
    msg = message.text.split()

    if not message.from_user or not (await message.chat.get_member(message.from_user.id)).status in ["administrator", "creator"]:
        await message.reply(get_message(lang, "NOT_ADMIN"))
        return

    if len(msg) != 2 or msg[1] not in ["enable", "disable"]:
        await message.reply(get_message(lang, "BIOSCAN_USAGE"))
        return

    status = msg[1] == "enable"
    await set_bioscan_status(message.chat.id, status)
    reply = get_message(lang, "BIOSCAN_ENABLED" if status else "BIOSCAN_DISABLED")
    await message.reply(reply)
