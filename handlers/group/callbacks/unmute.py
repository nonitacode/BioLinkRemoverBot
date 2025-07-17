# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ChatPermissions
from database.violations import clear_violations
from utils.language import get_message
from pyrogram.enums import ChatMemberStatus
from bot.bot import app

@app.on_callback_query(filters.regex(r"unmute_(\d+)"))
async def unmute_callback(client, query: CallbackQuery):
    chat_id = query.message.chat.id
    user_id = int(query.data.split("_")[1])

    admin = await client.get_chat_member(chat_id, query.from_user.id)
    if admin.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await query.answer("🚫 Only admins can unmute.", show_alert=True)
        return

    await auth_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"chat_id": chat_id, "user_id": user_id}},
        upsert=True
    )
    await reset_user(user_id, chat_id)

    try:
        await client.restrict_chat_member(
            chat_id,
            user_id,
            permissions=query.message.chat.permissions
        )
        await query.message.reply(f"✅ Approved and unmuted [user](tg://user?id={user_id}).")
    except Exception as e:
        await query.message.reply(f"❌ Failed to unmute: {e}")
