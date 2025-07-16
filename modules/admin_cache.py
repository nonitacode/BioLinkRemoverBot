# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

from pyrogram import filters
from bot.bot import bot
from database.group_admins_db import set_admins, clear_admins
from pyrogram.types import ChatMemberAdministrator

@bot.on_message(filters.command("admincache"))
async def cache_admins(client, message):
    if not message.chat or not message.chat.type.endswith("group"):
        return await message.reply("This command can only be used in groups.")
    
    chat_id = message.chat.id
    try:
        admins = await client.get_chat_members(chat_id, filter="administrators")
        admin_ids = [admin.user.id for admin in admins if admin.status in ("administrator", "creator")]
        set_admins(chat_id, admin_ids)
        await message.reply(f"✅ Cached {len(admin_ids)} group admins.")
    except Exception as e:
        await message.reply(f"❌ Failed to cache admins.\nError: {e}")

@bot.on_message(filters.command("clearcache"))
async def clear_admin_cache(client, message):
    if not message.chat or not message.chat.type.endswith("group"):
        return await message.reply("This command can only be used in groups.")
    
    chat_id = message.chat.id
    clear_admins(chat_id)
    await message.reply("✅ Admin cache cleared for this group.")
