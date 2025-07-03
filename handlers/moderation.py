from pyrogram import filters
from pyrogram.types import Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from config import LOG_CHANNEL
from database.core import is_whitelisted, increment_violations
from database.config import get_config
from utils.filters import contains_link


def init(app):
    @app.on_message(filters.group & filters.text)
    async def check_user_identity(_, message: Message):
        user = message.from_user
        chat_id = message.chat.id

        if not user or user.is_bot:
            return

        user_id = user.id

        try:
            # Skip scanning if user is admin or creator
            member = await app.get_chat_member(chat_id, user_id)
            if member.status in ("administrator", "creator"):
                await app.send_message(
                    LOG_CHANNEL,
                    f"✅ Skipped scan for admin: <a href='tg://user?id={user_id}'>{user.first_name}</a> [{user_id}] in <code>{chat_id}</code>"
                )
                return
        except Exception as e:
            print(f"[!] Failed to get member status: {e}")
            return

        if is_whitelisted(user_id):
            return

        try:
            identity_text = user.username or ""
            try:
                user_chat = await app.get_chat(user_id)
                if hasattr(user_chat, "bio") and user_chat.bio:
                    identity_text += f" {user_chat.bio}"
            except Exception as e:
                print(f"[!] Failed to get bio: {e}")

            if contains_link(identity_text):
                await message.delete()
                count = increment_violations(user_id)
                config = get_config(chat_id)
                limit = config['warn_limit']
                mode = config['punishment_mode']

                # Log the violation
                await app.send_message(
                    LOG_CHANNEL,
                    f"🚨 <b>Violation Detected</b>\n"
                    f"👤 <a href='tg://user?id={user_id}'>{user.first_name}</a> [<code>{user_id}</code>]\n"
                    f"🔗 <b>Bio/Username:</b> <code>{identity_text.strip()}</code>\n"
                    f"⚠️ <b>Warnings:</b> {count}/{limit}\n"
                    f"🗨 <b>Chat:</b> <code>{chat_id}</code>\n"
                    f"📝 <b>Message:</b> <code>{message.text[:100]}</code>"
                )

                if count >= limit:
                    if mode == "mute":
                        await message.chat.restrict_member(user_id, ChatPermissions(can_send_messages=False))
                    elif mode == "ban":
                        await message.chat.ban_member(user_id)

                    # Unmute button for admins
                    keyboard = InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔓 Unmute User", callback_data=f"unmute:{user_id}")]
                    ])

                    await message.reply(
                        f"🚫 <b>User Muted for Repeated Violations</b>\n"
                        f"👤 <a href='tg://user?id={user_id}'>{user.first_name}</a>\n"
                        f"⚠️ <b>Total Violations:</b> {count} / {limit}\n"
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
                        f"📌 <b>Warning Count:</b> {count} / {limit}\n"
                        f"🛑 Please remove links from your profile to avoid restrictions.",
                        quote=True
                    )

        except Exception as e:
            print(f"[!] Identity check failed for user {user_id}: {e}")
