from pyrogram import filters
from pyrogram.types import Message
from database.mongo import set_group_setting

@filters.command("settings") & filters.user(lambda _, __, m: m.from_user and m.from_user.is_chat_admin)
def settings_cmd(client, message: Message):
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) == 2:
        if args[1] in ["on", "off"]:
            set_group_setting(chat_id, "enabled", args[1] == "on")
            message.reply(f"⚙ Link scanning turned {'ON' if args[1] == 'on' else 'OFF'}.")
        else:
            message.reply("Usage: /settings [on|off]")
    else:
        message.reply("Usage: /settings [on|off]")
