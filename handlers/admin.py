from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from utils.sudo import is_sudo
from database.core import get_all_whitelist

def init(app):
    # /ping command
    @app.on_message(filters.command("ping"))
    async def ping(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 You are not authorized to use this.")
        await message.reply("🏓 <b>Pong!</b> Bot is alive and responding.")

    # /freelist command
    @app.on_message(filters.command("freelist"))
    async def freelist(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Only the bot owner can use this.")
        wl = get_all_whitelist()
        text = "\n".join([f"• <code>{uid}</code>" for uid in wl]) or "⚠️ No whitelisted users."
        await message.reply(f"✅ <b>Whitelisted Users:</b>\n{text}")

    # /broadcast command
    @app.on_message(filters.command("broadcast"))
    async def broadcast(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Not allowed.")

        if not message.reply_to_message:
            return await message.reply("📢 Reply to a message to broadcast it.")

        sent, failed = 0, 0
        # TODO: Replace with list of all chat_ids from DB
        broadcast_chats = [message.chat.id]  # Example: replace this with real chat IDs

        for chat_id in broadcast_chats:
            try:
                await app.copy_message(chat_id, message.chat.id, message.reply_to_message.message_id)
                sent += 1
            except:
                failed += 1

        await message.reply(f"📣 <b>Broadcast Completed</b>\n✅ Sent: {sent}\n❌ Failed: {failed}")

    # Inline callback for unmuting users
    @app.on_callback_query(filters.regex(r"^unmute:(\d+)$"))
    async def handle_unmute_callback(client, callback_query: CallbackQuery):
        user_id = int(callback_query.data.split(":")[1])
        chat_id = callback_query.message.chat.id

        # Only admins or OWNER_ID can unmute
        member = await client.get_chat_member(chat_id, callback_query.from_user.id)
        if not (member.status in ("administrator", "creator") or callback_query.from_user.id == OWNER_ID):
            return await callback_query.answer("🚫 Only admins can unmute this user.", show_alert=True)

        await client.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=True))

        await callback_query.edit_message_text(
            f"✅ <b>User Unmuted</b>\n"
            f"👤 <a href='tg://user?id={user_id}'>User</a> has been unmuted by admin <b>{callback_query.from_user.first_name}</b>."
        )
