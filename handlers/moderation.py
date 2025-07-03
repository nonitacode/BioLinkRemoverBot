from pyrogram import filters
from pyrogram.types import Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from utils.filters import contains_link
from database.core import is_whitelisted, increment_violations
from config import MAX_VIOLATIONS, LOG_CHANNEL

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
            identity_text = user.username or ""

            # Try getting user's bio (optional)
            try:
                user_chat = await app.get_chat(user_id)
                if hasattr(user_chat, "bio") and user_chat.bio:
                    identity_text += f" {user_chat.bio}"
            except:
                pass  # Fail silently if bio isn't accessible

            if contains_link(identity_text):
                await message.delete()
                count = increment_violations(user_id)

                # Log
                log_text = (
                    f"🚨 <b>Violation Detected</b>\n"
                    f"👤 <a href='tg://user?id={user_id}'>{user.first_name}</a> [<code>{user_id}</code>]\n"
                    f"🔗 Detected: <code>{identity_text.strip()}</code>\n"
                    f"⚠️ Warnings: {count}/{MAX_VIOLATIONS}\n"
                    f"🗨 Chat: <code>{chat_id}</code>\n"
                    f"📝 Message: <code>{message.text[:100]}</code>"
                )
                await app.send_message(LOG_CHANNEL, log_text)

                if count >= MAX_VIOLATIONS:
                    await message.chat.restrict_member(user_id, ChatPermissions(can_send_messages=False))

                    keyboard = InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔓 Unmute User", callback_data=f"unmute:{user_id}")]
                    ])

                    await message.reply(
                        f"🚫 <b>User Muted for Repeated Violations</b>\n"
                        f"👤 <a href='tg://user?id={user_id}'>{user.first_name}</a>\n"
                        f"⚠️ <b>Total Violations:</b> {count} / {MAX_VIOLATIONS}\n"
                        f"📛 <b>Reason:</b> Suspicious username or bio link detected.\n"
                        f"🔒 <b>Action Taken:</b> Muted in this group.",
                        reply_markup=keyboard,
                        quote=True
                    )
                else:
                    await message.reply(
                        f"⚠️ <b>Warning Issued</b>\n"
                        f"👤 <a href='tg://user?id={user_id}'>{user.first_name}</a>\n"
                        f"⚠️ <b>Violation:</b> Detected link or @username in profile.\n"
                        f"📌 <b>Warning Count:</b> {count} / {MAX_VIOLATIONS}\n"
                        f"🛑 Please remove links from your profile to avoid restrictions.",
                        quote=True
                    )

        except Exception as e:
            print(f"[!] Identity check failed for user {user_id}: {e}")
