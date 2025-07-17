from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from utils.language import get_message
from database.user_language import get_user_language
from database.auth_users import add_auth_user, remove_auth_user, get_auth_users
from database.warns import reset_warns
from pyrogram.enums import ChatMemberStatus

@app.on_message(filters.command("addauth") & filters.group)
async def add_auth(client, message: Message):
    lang = await get_user_language(message.from_user.id)

    if not message.reply_to_message:
        return await message.reply(get_message(lang, "reply_to_user"))

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    member = await client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return await message.reply(get_message(lang, "admin_only"))

    await add_auth_user(chat_id, user.id)
    await reset_warns(chat_id, user.id)

    await message.reply(get_message(lang, "auth_added").format(user=user.mention))

@app.on_message(filters.command("rmauth") & filters.group)
async def remove_auth(client, message: Message):
    lang = await get_user_language(message.from_user.id)

    if not message.reply_to_message:
        return await message.reply(get_message(lang, "reply_to_user"))

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    member = await client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return await message.reply(get_message(lang, "admin_only"))

    await remove_auth_user(chat_id, user.id)
    await message.reply(get_message(lang, "auth_removed").format(user=user.mention))

@app.on_message(filters.command("authusers") & filters.group)
async def list_auth_users(client, message: Message):
    lang = await get_user_language(message.from_user.id)
    chat_id = message.chat.id

    auth_users = await get_auth_users(chat_id)
    if not auth_users:
        return await message.reply(get_message(lang, "no_auth_users"))

    text = f"✅ **{get_message(lang, 'authorized_users')}**\n\n"
    for i, uid in enumerate(auth_users, 1):
        try:
            user = await client.get_users(uid)
            text += f"{i}. [{user.first_name}](tg://user?id={uid})\n"
        except:
            continue

    await message.reply(text, disable_web_page_preview=True)
