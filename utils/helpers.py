# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from pyrogram.errors import RPCError
from bot.bot import bot

async def is_user_admin(chat_id, user_id):
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.status in ("administrator", "creator")
    except RPCError:
        return False

async def mute_user(client, chat_id, user_id):
    try:
        await client.restrict_chat_member(
            chat_id, user_id,
            permissions={}
        )
    except Exception as e:
        print(f"❗ Mute error: {e}")
