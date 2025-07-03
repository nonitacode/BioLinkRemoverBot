# 🔒 LinkScanBot

Telegram bot to auto-moderate groups by deleting messages with links or @usernames, detecting suspicious bios, and auto-punishing repeat offenders.

## ✨ Features
- Delete messages containing links or usernames
- Scan new user bios for spam
- Auto-mute users after repeated violations
- Whitelist system
- Group-specific settings via `/settings`
- Log violations to a channel

## 🚀 Deploy Instructions

1. **Upgrade & Update:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```
2. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikchil/LinkScanBot && cd LinkScanBot
   ```
3. **Install Requirements**
   ```bash
   pip3 install -U -r requirements.txt
   ```
4. **Create .env  with sample.env**
   ```bash
   cp sample.env .env
   ```
   - Edit .env with your vars
5. **Editing Vars:**
   ```bash
   vi .env
   ```
   - Edit .env with your values.
   - Press `I` button on keyboard to start editing.
   - Press `Ctrl + C`  once you are done with editing vars and type `:wq` to save .env or `:qa` to exit editing.
6. **Installing tmux**
    ```bash
    sudo apt install tmux -y && tmux
    ```
7. **Run the Bot**
    ```bash
    bash start
    ```
### 🛠 Commands & Usage

👮 Admin Commands

Command	Description

/whitelist (reply)	✅ Whitelist a user so they can post links or usernames

/unwhitelist (reply)	❌ Remove user from whitelist

/settings on	🔒 Enable link scanning in the group

/settings off	🔓 Disable link scanning in the group

/broadcast -all (reply)	📢 Send a message to all groups and users

/broadcast -group (reply)	📣 Send a message to all groups only

/broadcast -user (reply)	📬 Send a message to all users only


> ⚠️ All commands must be used by group admins only.

### 🤖 Bot Behavior

Feature	Description

🔗 Auto-delete links & usernames	Removes messages containing URLs or @usernames instantly

👁 Bio scanner on join	Kicks/mutes users who have suspicious links/usernames in their bio

🔇 Auto-mute repeat offenders	After MAX_VIOLATIONS (default: 3), user is auto-muted

🧠 Smart permission check	Warns if the bot lacks delete/restrict permissions



---

### ⚙️ Setup (ENV Variables)

Variable	Description

API_ID / API_HASH	Your Telegram API credentials

BOT_TOKEN	Your bot token from BotFather

MONGO_URL	MongoDB connection URL

MAX_VIOLATIONS	Violations before auto-mute (default: 3)

LOG_CHANNEL	Channel ID where violations will be logged (optional)



---

### 💬 Examples

✅ Reply to a spammer with:
/whitelist

🔇 To turn off link scan:
/settings off

📣 To send an announcement:
/broadcast -all
