# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
from bot.bot import app
from config import LOG_CHANNEL

@app.on_chat_member_updated()
async def handle_chat_member(client, event: ChatMemberUpdated):
    # Ignore bots
    if event.new_chat_member and event.new_chat_member.user.is_bot:
        return

    # Detect user joined
    if event.new_chat_member and event.old_chat_member.status in ["left", "kicked"]:
        user = event.new_chat_member.user
        await app.send_message(
            LOG_CHANNEL,
            f"📥 <b>User Joined</b>\n"
            f"👤 <a href='tg://user?id={user.id}'>{user.first_name}</a>\n"
            f"🆔 <code>{user.id}</code>\n"
            f"💬 Chat: <b>{event.chat.title}</b>"
        )

    # Detect user left
    elif (
        event.old_chat_member
        and event.new_chat_member.status == "left"
        and event.old_chat_member.status != "left"
    ):
        user = event.old_chat_member.user
        await app.send_message(
            LOG_CHANNEL,
            f"📤 <b>User Left</b>\n"
            f"👤 <a href='tg://user?id={user.id}'>{user.first_name}</a>\n"
            f"🆔 <code>{user.id}</code>\n"
            f"💬 Chat: <b>{event.chat.title}</b>"
        )
