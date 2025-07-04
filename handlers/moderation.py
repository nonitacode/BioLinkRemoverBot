from pyrogram import filters
from pyrogram.types import Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from config import LOG_CHANNEL, OWNER_ID
from database.core import (
    is_whitelisted,
    increment_violations,
    remove_user_record,
    get_last_warn,
    set_last_warn,
    delete_last_warn,
    get_memory_config,
    get_bio_scan
)
from utils.filters import contains_link
from pyrogram.enums import ChatMemberStatus

def init(app):
    @app.on_message(filters.group & filters.text)
    async def check_user_identity(_, message: Message):
        user = message.from_user
        chat_id = message.chat.id

        if not user or user.is_bot:
            return

        if not get_bio_scan(chat_id):
            return

        user_id = user.id

        try:
            if user_id == OWNER_ID:
                remove_user_record(user_id)
                delete_last_warn(chat_id, user_id)
                return

            member = await app.get_chat_member(chat_id, user_id)
            if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                remove_user_record(user_id)
                delete_last_warn(chat_id, user_id)
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
                count = increment_violations(chat_id, user_id)
                config = get_memory_config(chat_id)
                limit = config['warn_limit']
                mode = config['punishment_mode']

                if count >= limit:
                    old_warn = get_last_warn(chat_id, user_id)
                    if old_warn and "message_id" in old_warn:
                        try:
                            await app.delete_messages(chat_id, old_warn["message_id"])
                        except:
                            pass
                    delete_last_warn(chat_id, user_id)

                    if mode == "mute":
                        await message.chat.restrict_member(user_id, ChatPermissions(can_send_messages=False))
                    elif mode == "ban":
                        await message.chat.ban_member(user_id)

                    keyboard = InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔓 Unmute User", callback_data=f"unmute:{user_id}")]
                    ])

                    user_mention = f"<a href='tg://user?id={user_id}'>{user.first_name}</a>"

                    await message.reply(
                        f"🚫 <b>User Muted for Repeated Violations</b>\n"
                        f"👤 {user_mention} (`{user_id}`)\n"
                        f"⚠️ <b>Total Violations:</b> {count} / {limit}\n"
                        f"📛 <b>Reason:</b> Suspicious username or bio link detected.\n"
                        f"🔒 <b>Action Taken:</b> Muted in this group.",
                        reply_markup=keyboard,
                        quote=True
                    )

                    if LOG_CHANNEL:
                        await app.send_message(
                            LOG_CHANNEL,
                            f"🚨 <b>Auto Mute Triggered</b>\n"
                            f"👤 User: {user_mention}\n"
                            f"🆔 User ID: <code>{user_id}</code>\n"
                            f"📍 Group: <code>{chat_id}</code>\n"
                            f"📛 Reason: Bio or username link\n"
                            f"🚫 Violations: {count} / {limit}"
                        )

                else:
                    old_warn = get_last_warn(chat_id, user_id)
                    if old_warn and "message_id" in old_warn:
                        try:
                            await app.delete_messages(chat_id, old_warn["message_id"])
                        except:
                            pass

                    user_mention = f"<a href='tg://user?id={user_id}'>{user.first_name}</a>"

                    warn_msg = await message.reply(
                        f"⚠️ <b>Warning Issued</b>\n"
                        f"👤 {user_mention} (`{user_id}`)\n"
                        f"⚠️ <b>Violation:</b> Detected link or @username in profile.\n"
                        f"📌 <b>Warning Count:</b> {count} / {limit}\n"
                        f"🛑 Please remove links from your profile to avoid restrictions.",
                        quote=True
                    )
                    set_last_warn(chat_id, user_id, warn_msg.id)

                    if LOG_CHANNEL:
                        await app.send_message(
                            LOG_CHANNEL,
                            f"⚠️ <b>Warning Logged</b>\n"
                            f"👤 {user_mention}\n"
                            f"🆔 User ID: <code>{user_id}</code>\n"
                            f"📍 Group: <code>{chat_id}</code>\n"
                            f"⚠️ Violations: {count} / {limit}"
                        )

        except Exception as e:
            print(f"[!] Identity check failed for user {user_id}: {e}")

    # ✅ UNMUTE BUTTON HANDLER
    @app.on_callback_query(filters.regex(r"^unmute:(\d+)$"))
    async def handle_unmute(client, callback_query):
        user_id = int(callback_query.data.split(":")[1])
        chat_id = callback_query.message.chat.id

        try:
            await client.restrict_chat_member(
                chat_id,
                user_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_polls=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False
                )
            )
            remove_user_record(user_id)

            user_info = await client.get_users(user_id)
            user_mention = f"<a href='tg://user?id={user_id}'>{user_info.first_name}</a>"

            await callback_query.answer("✅ User has been unmuted and warnings reset.", show_alert=True)
            await callback_query.message.edit_text(
                f"🔓 <b>User Unmuted</b>\n"
                f"👤 {user_mention} (`{user_id}`) has been unmuted and warnings cleared."
            )
        except Exception as e:
            await callback_query.answer("❌ Failed to unmute.", show_alert=True)
            print(f"[!] Failed to unmute user {user_id}: {e}")
