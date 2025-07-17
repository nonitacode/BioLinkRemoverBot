# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from database.violations import clear_violations
from utils.language import get_message
from pyrogram.enums import ChatMemberStatus

@Client.on_callback_query(filters.regex("unmute_"))
async def unmute_callback(client, query: CallbackQuery):
    user_id = int(query.data.split("_")[1])
    chat_id = query.message.chat.id

    member = await client.get_chat_member(chat_id, query.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await query.answer("❌ Only admins can unmute.", show_alert=True)

    try:
        await client.restrict_chat_member(chat_id, user_id, permissions={
            "can_send_messages": True,
            "can_send_media_messages": True,
            "can_send_polls": True,
            "can_send_other_messages": True,
            "can_add_web_page_previews": True,
            "can_change_info": False,
            "can_invite_users": True,
            "can_pin_messages": False
        })
        clear_violations(chat_id, user_id)
        await query.answer("✅ User unmuted successfully!", show_alert=True)
        await query.message.delete()
    except:
        await query.answer("❌ Failed to unmute.", show_alert=True)
