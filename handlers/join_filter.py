from pyrogram.types import ChatMemberUpdated
from database.core import is_whitelisted
from utils.filters import contains_link

def init(app):
    @app.on_chat_member_updated()
    async def scan_bio(_, member: ChatMemberUpdated):
        if member.new_chat_member.user.is_bot:
            return
        user = member.new_chat_member.user
        if is_whitelisted(user.id):
            return
        bio = f"{user.username or ''} {user.bio or ''}"
        if contains_link(bio):
            try:
                await app.ban_chat_member(member.chat.id, user.id)
                await app.send_message(member.chat.id, f"🚨 Removed suspicious user @{user.username}")
            except Exception:
                await app.send_message(member.chat.id, "❗ Could not remove suspicious user.")
