import time
import asyncio
from datetime import timedelta

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.enums import ChatMembersFilter

from config import OWNER_ID, LOG_CHANNEL, BOT_NAME
from utils.sudo import is_sudo
from database.core import (
    refresh_memory_cache,
    get_served_users,
    get_served_chats,
    add_served_user,
    add_served_chat,
)

BOT_START_TIME = time.time()
BOT_USERNAME = "BioLinkRemoverBot"  # Update as needed

BROADCAST_STATUS = {
    "active": False,
    "sent": 0,
    "failed": 0,
    "total": 0,
    "start_time": 0,
    "users": 0,
    "chats": 0,
    "sent_users": 0,
    "sent_chats": 0,
    "mode": "",
}


def init(app):

    # ✅ Log every command + /start
    @app.on_message(filters.command)
    async def log_all_commands(client, message: Message):
        if not LOG_CHANNEL or not message.from_user:
            return

        user = message.from_user
        user_mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
        origin = "🗣 <b>Group</b>" if message.chat.type in ["group", "supergroup"] else "👤 <b>Private</b>"
        chat_info = f"\n👥 <b>Chat:</b> <code>{message.chat.title}</code>" if message.chat.title else ""

        await client.send_message(
            LOG_CHANNEL,
            f"📥 <b>Command Used</b>\n"
            f"{origin}{chat_info}\n"
            f"👤 <b>User:</b> {user_mention} (`{user.id}`)\n"
            f"💬 <b>Command:</b> <code>{message.text}</code>"
        )

    # ✅ /ping with uptime
    @app.on_message(filters.command("ping"))
    async def ping(_, message: Message):
        start = time.time()
        sent = await message.reply("🏓 Pinging...")
        end = time.time()
        latency = round((end - start) * 1000)
        uptime = str(timedelta(seconds=int(time.time() - BOT_START_TIME)))

        await sent.edit_text(
            f"🏓 <b>Bot Status</b>\n"
            f"📶 <b>Ping:</b> <code>{latency}ms</code>\n"
            f"⏱ <b>Uptime:</b> <code>{uptime}</code>\n"
            f"🤖 <b>Bot:</b> @{BOT_USERNAME}"
        )

    # ✅ /refresh memory cache
    @app.on_message(filters.command("refresh"))
    async def refresh_cmd(_, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 You are not allowed to do this.")
        refresh_memory_cache()
        await message.reply("🔄 <b>System Synced</b>\nAll data refreshed and up-to-date.")

        if LOG_CHANNEL:
            await _.send_message(
                LOG_CHANNEL,
                f"♻️ <b>Memory Cache Refreshed</b>\n"
                f"👤 <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
            )

    # ✅ /admincache to resync admin list
    @app.on_message(filters.command("admincache") & filters.group)
    async def admin_cache_cmd(client, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 You are not allowed to do this.")
        try:
            members = []
            async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
                members.append(member.user.id)

            await message.reply(
                f"👥 <b>Admin List Refreshed</b>\n"
                f"Total admins synced: <code>{len(members)}</code>"
            )

            if LOG_CHANNEL:
                await client.send_message(
                    LOG_CHANNEL,
                    f"🔁 <b>AdminCache Updated</b>\n"
                    f"👤 By: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n"
                    f"👥 Group: <code>{message.chat.title}</code>\n"
                    f"👮 Admins Synced: <code>{len(members)}</code>"
                )

        except ChatAdminRequired:
            await message.reply("❌ I need admin rights to view admin list.")

    # ✅ /broadcast command
    @app.on_message(filters.command("broadcast"))
    async def broadcast_command(client, message: Message):
        if not is_sudo(message.from_user.id):
            return await message.reply("🚫 Not authorized.")

        cmd = message.text.lower()
        mode = "forward" if "-forward" in cmd else "copy"

        if "-all" in cmd:
            users = await get_served_users()
            chats = await get_served_chats()
            target_users = [u["user_id"] for u in users]
            target_chats = [c["chat_id"] for c in chats]
        elif "-user" in cmd or "-users" in cmd:
            users = await get_served_users()
            target_users = [u["user_id"] for u in users]
            target_chats = []
        elif "-group" in cmd or "-chats" in cmd:
            chats = await get_served_chats()
            target_users = []
            target_chats = [c["chat_id"] for c in chats]
        else:
            return await message.reply("Usage: /broadcast -all|-user|-group [-forward]")

        if message.reply_to_message:
            content = message.reply_to_message
        else:
            text = message.text
            for kw in ["/broadcast", "-forward", "-all", "-users", "-user", "-chats", "-group"]:
                text = text.replace(kw, "")
            content = text.strip()
            if not content:
                return await message.reply("📝 Provide a message or reply to one.")

        total = len(target_users) + len(target_chats)
        BROADCAST_STATUS.update({
            "active": True,
            "sent": 0,
            "failed": 0,
            "total": total,
            "start_time": time.time(),
            "users": len(target_users),
            "chats": len(target_chats),
            "sent_users": 0,
            "sent_chats": 0,
            "mode": mode,
        })

        msg = await message.reply("📡 Broadcast started...")

        async def deliver(chat_id):
            try:
                if isinstance(content, str):
                    await client.send_message(chat_id, content)
                elif mode == "forward":
                    await client.forward_messages(chat_id, message.chat.id, [content.id])
                else:
                    await content.copy(chat_id)
                BROADCAST_STATUS["sent"] += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
                return await deliver(chat_id)
            except Exception:
                BROADCAST_STATUS["failed"] += 1

        targets = target_users + target_chats
        for i in range(0, total, 100):
            batch = targets[i:i + 100]
            await asyncio.gather(*(deliver(cid) for cid in batch))
            await asyncio.sleep(1)

        elapsed = round(time.time() - BROADCAST_STATUS["start_time"])
        await msg.edit_text(
            f"✅ <b>Broadcast Complete</b>\n"
            f"📦 Total: {total}\n"
            f"✅ Sent: {BROADCAST_STATUS['sent']}\n"
            f"❌ Failed: {BROADCAST_STATUS['failed']}\n"
            f"⏱ Time: {elapsed}s"
        )
        BROADCAST_STATUS["active"] = False

        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"📢 <b>Broadcast Sent</b>\n"
                f"👤 <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n"
                f"📦 Total: {total} | ✅ Sent: {BROADCAST_STATUS['sent']} | ❌ Failed: {BROADCAST_STATUS['failed']}"
            )

    # ✅ /status
    @app.on_message(filters.command("status"))
    async def status_command(_, message: Message):
        if not BROADCAST_STATUS["active"]:
            return await message.reply("📡 No active broadcast.")
        percent = round((BROADCAST_STATUS["sent"] + BROADCAST_STATUS["failed"]) / BROADCAST_STATUS["total"] * 100, 2)
        await message.reply(
            f"📊 Broadcast Progress:\n"
            f"✅ Sent: {BROADCAST_STATUS['sent']}\n"
            f"❌ Failed: {BROADCAST_STATUS['failed']}\n"
            f"📦 Total: {BROADCAST_STATUS['total']}\n"
            f"🔃 Progress: {percent}%"
        )

    # ✅ Track users/groups for broadcast
    @app.on_message(filters.private & ~filters.service)
    async def save_user(_, message: Message):
        await add_served_user(message.from_user.id)

    @app.on_chat_member_updated()
    async def save_group(_, chat_member):
        await add_served_chat(chat_member.chat.id)
