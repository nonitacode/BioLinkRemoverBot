# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

from database.stats_db import update_bot_stats, get_bot_stats

@bot.on_message(filters.command("stats"))
async def stats(client, message):
    """Show bot statistics."""
    users_count, groups_count = get_bot_stats()
    stats_message = f"Bot Statistics:\n\nUsers: {users_count}\nGroups: {groups_count}"
    await message.reply(stats_message)

@bot.on_message(filters.command("update_stats"))
async def update_stats(client, message):
    """Update bot statistics manually."""
    users_count = get_users_count()
    groups_count = get_groups_count()
    update_bot_stats(users_count, groups_count)
    await message.reply("Bot statistics updated.")
