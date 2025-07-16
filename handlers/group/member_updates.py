# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram.types import ChatMemberUpdated
from pyrogram import filters
from bot.bot import bot
from config import LOG_CHANNEL

@bot.on_chat_member_updated()
async def handle_chat_member(client, event: ChatMemberUpdated):
    if event.new_chat_member and event.new_chat_member.user.is_bot:
        return

    if event.new_chat_member:
        user = event.new_chat_member.user
        await bot.send_message(
            LOG_CHANNEL,
            f"#JOINED\nUser: [{user.first_name}](tg://user?id={user.id})\nChat: {event.chat.title}"
        )
    elif event.old_chat_member and event.old_chat_member.status != "left" and event.new_chat_member.status == "left":
        user = event.old_chat_member.user
        await bot.send_message(
            LOG_CHANNEL,
            f"#LEFT\nUser: [{user.first_name}](tg://user?id={user.id})\nChat: {event.chat.title}"
        )
