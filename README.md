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
