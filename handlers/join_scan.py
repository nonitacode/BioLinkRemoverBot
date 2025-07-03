from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
from filters.link_detector import contains_link
from database.mongo import take_action

@filters.chat_member_updated
def bio_checker(client, update: ChatMemberUpdated):
    user = update.new_chat_member.user
    if user and contains_link(user.bio):
        take_action(client, update.chat.id, user.id)
