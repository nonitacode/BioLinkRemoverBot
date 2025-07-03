from pyrogram import filters
from pyrogram.types import Message
from database.mongo import is_whitelisted

@filters.new_chat_members
def bio_checker(client, message: Message):
    for user in message.new_chat_members:
        bio = user.bio or ""
        username = user.username or ""
        if any(x in bio.lower() for x in ["http", ".me", "t.me", "@", ".com"]) or "@" in username:
            if not is_whitelisted(message.chat.id, user.id):
                try:
                    client.restrict_chat_member(
                        message.chat.id,
                        user.id,
                        permissions={}
                    )
                    message.reply_text(f"🚫 {user.mention} muted due to suspicious bio/username.")
                except:
                    pass
