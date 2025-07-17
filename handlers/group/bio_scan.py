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
settings_col = db["group_settings"]

# Regex pattern for bio scan
LINK_PATTERN = re.compile(r"(t\.me\/\w+|https?://\S+|@\w+)", re.IGNORECASE)


# ---------- Helpers ----------

async def is_authorized(user_id: int, chat_id: int) -> bool:
    return await auth_col.find_one({"chat_id": chat_id, "user_id": user_id}) is not None


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


async def is_scan_enabled(chat_id: int) -> bool:
    doc = await settings_col.find_one({"chat_id": chat_id})
    return doc and doc.get("bioscan_enabled", False)


# ---------- Commands ----------

@app.on_message(filters.command("bioscan") & filters.group)
async def bioscan_toggle(client, message: Message):
    if not message.from_user:
        return

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply("🚫 Only group admins can use this command.")
        return

    if len(message.command) < 2:
        await message.reply("⚙️ Usage: `/bioscan enable` or `/bioscan disable`", quote=True)
        return

    action = message.command[1].lower()
    if action == "enable":
        await settings_col.update_one(
            {"chat_id": message.chat.id},
            {"$set": {"bioscan_enabled": True}},
            upsert=True
        )
        await message.reply("✅ Bio scan is now **enabled** for this group.")
    elif action == "disable":
        await settings_col.update_one(
            {"chat_id": message.chat.id},
            {"$set": {"bioscan_enabled": False}},
            upsert=True
        )
        await message.reply("🚫 Bio scan is now **disabled** for this group.")
    else:
        await message.reply("⚠️ Invalid option. Use `/bioscan enable` or `/bioscan disable`.")


@app.on_message(filters.group & filters.text)
async def scan_bio(client, message: Message):
    user = message.from_user
    chat = message.chat
    if not user or not chat:
        return

    if not await is_scan_enabled(chat.id):
        return  # Do nothing if bioscan is disabled

    # Admins are auto-authorized
    member = await client.get_chat_member(chat.id, user.id)
    if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await auth_col.update_one(
            {"chat_id": chat.id, "user_id": user.id},
            {"$set": {"chat_id": chat.id, "user_id": user.id}},
            upsert=True
        )
        return

    # Check authorization
    if await is_authorized(user.id, chat.id):
        return

    # Scan username (can't scan bio unless private chat)
    bio_text = (user.username or "") + " " + (user.first_name or "") + " " + (user.last_name or "")
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
                    f"🚫 **Muted {user.mention}**\n"
                    f"👤 Name: {user.first_name}\n"
                    f"📌 Reason: Promoting usernames/links in profile.\n"
                    f"✅ Solve: Ask admin to approve you.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("✅ Unmute", callback_data=f"unmute_{user.id}")
                    ]])
                )
            except Exception as e:
                print(f"Failed to mute: {e}")
        else:
            await message.reply(
                f"⚠️ **Warning {warn_count}/3** to {user.mention}\n"
                f"👤 Name: {user.first_name}\n"
                f"📌 Reason: Link or username found in bio/username.\n"
                f"✅ Solve: Ask admin to approve you with /addauth"
            )


@app.on_message(filters.command("addauth") & filters.group)
async def add_auth_user(client, message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        await message.reply("🔁 Reply to the user you want to approve.")
        return

    await auth_col.update_one(
        {"chat_id": message.chat.id, "user_id": user.id},
        {"$set": {"chat_id": message.chat.id, "user_id": user.id}},
        upsert=True
    )
    await reset_user(user.id, message.chat.id)

    try:
        await client.restrict_chat_member(
            message.chat.id,
            user.id,
            permissions=message.chat.permissions
        )
    except Exception as e:
        await message.reply(f"⚠️ Failed to unmute: {e}")
        return

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
