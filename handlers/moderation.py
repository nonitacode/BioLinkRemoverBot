from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
from utils.filters import contains_link
from database.core import (
    is_whitelisted,
    increment_violations,
)
from config import MAX_VIOLATIONS

def init(app):
    @app.on_message(filters.group & filters.text)
    async def check_user_identity(_, message: Message):
        user = message.from_user
        chat_id = message.chat.id

        if not user or user.is_bot:
            return

        user_id = user.id

        if is_whitelisted(user_id):
            return

        try:
            user_info = await app.get_users(user_id)
            identity_text = f"{user_info.username or ''} {user_info.bio or ''}"

            if contains_link(identity_text):
                await message.delete()
                count = increment_violations(user_id)

                if count >= MAX_VIOLATIONS:
                    await message.chat.restrict_member(user_id, ChatPermissions(can_send_messages=False))
                    await message.reply(f"🚫 <b>User muted</b> due to {count} violations.")
                else:
                    await message.reply(
                        f"⚠️ <b>Warning {count}/{MAX_VIOLATIONS}:</b> Your profile contains links or usernames. Please remove them to avoid restrictions."
                    )
        except Exception as e:
            await message.reply(f"⚠️ Could not check user bio.\n<code>{e}</code>")
