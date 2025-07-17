from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from database.whitelist import add_to_whitelist, remove_from_whitelist, get_whitelisted_users
from database.violations import clear_violations

@Client.on_message(filters.command("addauth") & filters.group)
async def add_authorized(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to the user to authorize them.")

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("❌ Only admins can use this command.")

    user = message.reply_to_message.from_user
    add_to_whitelist(message.chat.id, user.id)
    clear_violations(message.chat.id, user.id)

    await message.reply(f"✅ {user.mention} has been authorized. Previous violations reset.")

@Client.on_message(filters.command("rmauth") & filters.group)
async def remove_authorized(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to the user to remove them from whitelist.")

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("❌ Only admins can use this command.")

    user = message.reply_to_message.from_user
    remove_from_whitelist(message.chat.id, user.id)

    await message.reply(f"❌ {user.mention} removed from whitelist.")

@Client.on_message(filters.command("authusers") & filters.group)
async def show_auth_users(client, message: Message):
    users = get_whitelisted_users(message.chat.id)
    if not users:
        return await message.reply("⚠️ No users are whitelisted in this group.")
    
    lines = [f"🔹 [{uid}](tg://user?id={uid})" for uid in users]
    await message.reply("**✅ Authorized Users:**\n\n" + "\n".join(lines), disable_web_page_preview=True)
