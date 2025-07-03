from pyrogram.types import Chat

async def check_permissions(bot, chat: Chat):
    member = await bot.get_chat_member(chat.id, bot.me.id)
    return member.can_delete_messages and member.can_restrict_members
