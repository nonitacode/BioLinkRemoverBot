from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from utils.sudo import is_sudo
from database.core import get_all_whitelist
from database.config import get_config, set_warn_limit, set_punishment_mode


def init(app):
    @app.on_message(filters.command("ping"))
    async def ping(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 You are not authorized to use this.")
        await message.reply("🏓 <b>Pong!</b> Bot is alive and responding.")

    @app.on_message(filters.command("freelist"))
    async def freelist(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Only the bot owner can use this.")
        wl = get_all_whitelist()
        text = "\n".join([f"• <code>{uid}</code>" for uid in wl]) or "⚠️ No whitelisted users."
        await message.reply(f"✅ <b>Whitelisted Users:</b>\n{text}")

    @app.on_message(filters.command("broadcast"))
    async def broadcast(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Not allowed.")

        if not message.reply_to_message:
            return await message.reply("📢 Reply to a message to broadcast it.")

        sent, failed = 0, 0
        broadcast_chats = [message.chat.id]  # Replace with real chat list

        for chat_id in broadcast_chats:
            try:
                await app.copy_message(chat_id, message.chat.id, message.reply_to_message.message_id)
                sent += 1
            except:
                failed += 1

        await message.reply(f"📣 <b>Broadcast Completed</b>\n✅ Sent: {sent}\n❌ Failed: {failed}")

    @app.on_message(filters.command("config") & filters.group)
    async def config_command(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Only bot owner can use this.")

        chat_id = message.chat.id
        config = get_config(chat_id)

        text = (
            f"🛠️ <b>Group Configuration</b>\n\n"
            f"⚠️ <b>Warn Limit:</b> {config['warn_limit']}\n"
            f"🔨 <b>Punishment:</b> {config['punishment_mode'].capitalize()}\n\n"
            f"Use the buttons below to update settings."
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Increase Warn Limit", callback_data=f"cfg:warn_inc:{chat_id}")],
            [InlineKeyboardButton("➖ Decrease Warn Limit", callback_data=f"cfg:warn_dec:{chat_id}")],
            [InlineKeyboardButton("🔒 Set Punishment: Mute", callback_data="cfg:punish:mute")],
            [InlineKeyboardButton("🚫 Set Punishment: Ban", callback_data="cfg:punish:ban")],
            [InlineKeyboardButton("⚠️ Set Punishment: Warn Only", callback_data="cfg:punish:warn")]
        ])

        await message.reply(text, reply_markup=keyboard)

    @app.on_callback_query(filters.regex(r"^cfg:(warn_inc|warn_dec):(-?\d+)$"))
    async def update_warn_limit(client, cb: CallbackQuery):
        action, chat_id = cb.data.split(":")[1:]
        chat_id = int(chat_id)

        if not is_sudo(cb.from_user.id):
            return await cb.answer("❌ Not allowed.", show_alert=True)

        config = get_config(chat_id)
        current = config["warn_limit"]
        new_limit = current + 1 if action == "warn_inc" else max(1, current - 1)

        set_warn_limit(chat_id, new_limit)
        await cb.answer(f"✅ Warn limit set to {new_limit}.", show_alert=True)
        await cb.message.delete()
        await config_command(client, cb.message)

    @app.on_callback_query(filters.regex(r"^cfg:punish:(mute|ban|warn)$"))
    async def update_punishment_mode(client, cb: CallbackQuery):
        mode = cb.data.split(":")[2]

        if not is_sudo(cb.from_user.id):
            return await cb.answer("❌ Not allowed.", show_alert=True)

        set_punishment_mode(cb.message.chat.id, mode)
        await cb.answer(f"✅ Punishment mode set to: {mode.capitalize()}", show_alert=True)
        await cb.message.delete()
        await config_command(client, cb.message)

    @app.on_callback_query(filters.regex(r"^unmute:(\d+)$"))
    async def handle_unmute_callback(client, callback_query: CallbackQuery):
        user_id = int(callback_query.data.split(":")[1])
        chat_id = callback_query.message.chat.id

        member = await client.get_chat_member(chat_id, callback_query.from_user.id)
        if not (member.status in ("administrator", "creator") or callback_query.from_user.id == OWNER_ID):
            return await callback_query.answer("🚫 Only admins can unmute this user.", show_alert=True)

        await client.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=True))

        await callback_query.edit_message_text(
            f"✅ <b>User Unmuted</b>\n"
            f"👤 <a href='tg://user?id={user_id}'>User</a> has been unmuted by admin <b>{callback_query.from_user.first_name}</b>."
        )
