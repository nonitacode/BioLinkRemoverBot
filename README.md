<p align="center">
  <img src="https://raw.githubusercontent.com/Nikchil/BioLinkRemoverBot/refs/heads/main/assets/biolinkremoverbot.png" alt="Bio Link Remover Logo" width="250"/>
</p>

<h1 align="center">🔒 BioLinkRemoverBot</h1>

<p align="center">
Telegram bot to <strong>auto-moderate groups</strong> by deleting messages with links or @usernames, detecting suspicious bios, and auto-punishing repeat offenders.
</p>

---

## ✨ Features

- 🔗 Delete messages containing **links or usernames**
- 👁 Scan new user bios for **spam content**
- 🔇 Auto-mute users after repeated **violations**
- ✅ Whitelist system for **trusted users**
- ⚙️ Group-specific settings via `/settings`
- 📝 Log violations to a **channel**

---

## 🚀 Deploy Instructions

### 1. 🔄 Upgrade & Update
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

### 2. 📥 Clone the Repository
```bash
git clone https://github.com/Nikchil/BioLinkRemoverBot && cd BioLinkRemoverBot
```

### 3. 📦 Install Requirements
```bash
pip3 install -U -r requirements.txt
```

### 4. ⚙️ Create `.env` File
```bash
cp sample.env .env
```
- Open `.env` and edit it with your values.

### 5. 📝 Edit ENV Vars
```bash
vi .env
```
- Press `I` to start editing.
- After changes: Press `Ctrl + C` and type `:wq` to save or `:qa` to quit.

### 6. 🔧 Install tmux
```bash
sudo apt install tmux -y && tmux
```

### 7. 🚀 Run the Bot
```bash
bash start
```

---

## 🛠 Commands & Usage

### 👮 Admin Commands

| Command | Description |
|--------|-------------|
| `/allow` (mention, ID or reply) | ✅ Whitelist a user |
| `/unwhitelist` (reply) | ❌ Remove from whitelist |
| `/settings on` | 🔒 Enable link scanning |
| `/settings off` | 🔓 Disable link scanning |
| `/broadcast -all` (reply) | 📢 Send message to all groups/users |
| `/broadcast -group` (reply) | 📣 Send to groups only |
| `/broadcast -user` (reply) | 📬 Send to users only |

> ⚠️ All commands are restricted to **group admins**.

---

## 🤖 Bot Behavior

| Feature | Description |
|--------|-------------|
| 🔗 Auto-delete links/usernames | Removes messages with links or `@usernames` |
| 👁 Bio scanner | Kicks or mutes users with suspicious bio content |
| 🔇 Auto-mute | After `MAX_VIOLATIONS` (default: 3) |
| 🧠 Smart permission check | Warns if bot lacks delete/restrict permissions |

---

## ⚙️ Setup (ENV Variables)

| Variable | Description |
|----------|-------------|
| `API_ID` / `API_HASH` | Telegram API credentials |
| `BOT_TOKEN` | Bot token from BotFather |
| `MONGO_URL` | MongoDB connection string |
| `MAX_VIOLATIONS` | Violations before mute (default: 3) |
| `LOG_CHANNEL` | Log channel ID (optional) |

---

## 💬 Usage Examples

```bash
✅ /whitelist        → Reply to a spammer to whitelist
🔇 /settings off     → Disable link scanning
📣 /broadcast -all   → Send an announcement
```

---

## 🔄 Updates & Support

Stay updated with new features and releases:

<p align="center">
  <a href="https://telegram.me/GrayBotSupport">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://telegram.me/GrayBots">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

## 🤝 Contributing

We welcome all contributions to improve this bot!  

To contribute:

1. 🍴 Fork the repository  
2. 🌿 Create a new branch  
3. 💻 Make your changes  
4. 📥 Commit with clear messages  
5. 📤 Submit a pull request  

For help, reach out via our support group on Telegram.

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.
