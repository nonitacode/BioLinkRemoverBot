# BioLinkRemoverBot - All rights reserved
# © Graybots™. All rights reserved.

import re
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus
from bot.bot import app
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

# Mongo Setup
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["BioLinkRemover"]
warns_col = db["warns"]
auth_col = db["auth_users"]

# Regex pattern for bio scan
LINK_PATTERN = re.compile(r"(t\.me\/\w+|https?://\S+|@\w+)", re.IGNORECASE)


async def is_authorized(user_id: int, chat_id: int) -> bool:
    auth = await auth_col.find_one({"chat_id": chat_id, "user_id": user_id})
    return bool(auth)


async def add_warn(user_id: int, chat_id: int) -> int:
    existing = await warns_col.find_one({"chat_id": chat_id, "user_id": user_id}) or {}
    count = existing.get("warns", 0) + 1
    await warns_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"warns": count}},
        upsert=True
    )
    return count


async def reset_user(user_id: int, chat_id: int):
    await warns_col.delete_one({"chat_id": chat_id, "user_id": user_id})
    await auth_col.delete_one({"chat_id": chat_id, "user_id": user_id})


@app.on_message(filters.group & filters.text)
async def scan_bio(client, message: Message):
    user = message.from_user
    chat = message.chat

    if not user or not user.id or not chat.id:
        return

    # Check admin status
    member = await client.get_chat_member(chat.id, user.id)
    if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await auth_col.update_one(
            {"chat_id": chat.id, "user_id": user.id},
            {"$set": {"chat_id": chat.id, "user_id": user.id}},
            upsert=True
        )
        return  # Auto-authorize admins

    # Check authorization
    if await is_authorized(user.id, chat.id):
        return

    # Scan bio and username
    user_info = await client.get_chat(user.id)
bio_text = (user_info.bio or "") + " " + (user_info.username or "")
    if LINK_PATTERN.search(bio_text):
        warn_count = await add_warn(user.id, chat.id)

        if warn_count >= 3:
            try:
                await client.restrict_chat_member(
                    chat.id,
                    user.id,
                    permissions=chat.permissions.__class__(can_send_messages=False)
                )
                await message.reply(
                    f"🚫 **Muted {user.mention}**\n\n"
                    f"👤 Name: {user.first_name}\n"
                    f"📌 Reason: Promoting links/usernames in bio.\n"
                    f"✅ Solve: Ask admin to approve you.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("✅ Unmute", callback_data=f"unmute_{user.id}")
                    ]])
                )
            except Exception as e:
                print(f"Failed to mute: {e}")
        else:
            await message.reply(
                f"⚠️ **Warning {warn_count}/3** to {user.mention}\n\n"
                f"👤 Name: {user.first_name}\n"
                f"📌 Reason: Link or username found in bio.\n"
                f"✅ Solve: Ask admin to approve you with /addauth",
            )


@app.on_message(filters.command("addauth") & filters.group)
async def add_auth_user(client, message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        await message.reply("Reply to the user you want to approve.")
        return

    await auth_col.update_one(
        {"chat_id": message.chat.id, "user_id": user.id},
        {"$set": {"chat_id": message.chat.id, "user_id": user.id}},
        upsert=True
    )
    await reset_user(user.id, message.chat.id)

    await client.restrict_chat_member(
        message.chat.id,
        user.id,
        permissions=message.chat.permissions
    )

    await message.reply(f"✅ {user.mention} is now approved and unmuted.")


@app.on_callback_query(filters.regex(r"unmute_(\d+)"))
async def unmute_callback(client, query: CallbackQuery):
    user_id = int(query.data.split("_")[1])
    chat_id = query.message.chat.id

    admin = await client.get_chat_member(chat_id, query.from_user.id)
    if admin.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await query.answer("Only admins can unmute.", show_alert=True)
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
