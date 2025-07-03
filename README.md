
<p align="center">
  <img src="https://raw.githubusercontent.com/Nikchil/BioLinkRemoverBot/refs/heads/main/assets/biolinkremoverbot.png" alt="Bio Link Remover Logo" width="250"/>
</p>

<h1 align="center">🔒 BioLinkRemoverBot</h1>

<p align="center">
A smart and powerful Telegram bot to <strong>auto-moderate groups</strong> by detecting suspicious usernames or bios, removing promotional links, and punishing spammy users automatically.
</p>

---

## ✨ Features

- 🔗 Auto-delete **links or @usernames** from messages
- 👁 Smart scan of **user bios** for spam, usernames, and links
- 🧠 Auto-detect if user is an **admin or owner** and skip moderation
- ⛔ Issue **warnings** and auto-apply punishments on repeated violations
- 🔇 Auto-mute or ban users after configurable limits
- ✅ `/allow` system to **whitelist trusted users**
- ⚙️ Group-specific settings panel via `/config`
- 📢 `/broadcast` to announce updates across all groups
- 🧾 Violation logging to a **log channel**
- 🔓 Inline **unmute buttons** for group admins

---

## 🛠 Commands & Usage

### 👑 Admin / Sudo Commands

| Command           | Description |
|-------------------|-------------|
| `/ping`           | Check if bot is online (Sudo only) |
| `/broadcast`      | Broadcast a replied message to all chats (Sudo only) |
| `/allow <user>`   | Whitelist a user (mention, reply or ID) |
| `/remove <user>`  | Remove user from whitelist |
| `/allowlist`      | Show all allowed (whitelisted) users |
| `/config`         | Group config panel for warn limit & punishment |
| `/start`          | Show welcome message |
| `/help`           | Show full bot usage guide |

> ⚠️ Admins and owners are automatically whitelisted and not punished.

---

## 🤖 Bot Behavior

| Feature               | Behavior |
|-----------------------|----------|
| 🔗 Link Detection     | Deletes any message with a URL or @username |
| 👤 Bio Scanning       | Scans user bios on each message — warns if username/link found |
| ⚠️ Warnings           | User gets warned up to set limit (default: 3) |
| 🔇 Auto Mute          | After exceeding limit, the bot will mute or ban user |
| ✅ Whitelist Bypass   | Whitelisted users are never warned or punished |
| 🔒 Smart Admin Check  | Admins/owners are auto-freed from moderation |
| 🧠 Violation Memory   | Tracks warnings via MongoDB and restores if user is removed from whitelist |
| 🎛 Configurable       | All punishments and limits adjustable via inline `/config` menu |

---

## 💻 Deploy Instructions

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

### 4. ⚙️ Setup Environment
```bash
cp sample.env .env
vi .env
```
- Add your `API_ID`, `API_HASH`, `BOT_TOKEN`, `MONGO_URL`, etc.

### 5. ▶️ Run the Bot
```bash
tmux
bash start
```

---

## ⚙️ ENV Variables

| Variable        | Description |
|------------------|-------------|
| `API_ID`         | Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH`       | Telegram API hash |
| `BOT_TOKEN`      | Bot token from [@BotFather](https://t.me/BotFather) |
| `MONGO_URL`      | MongoDB connection string |
| `OWNER_ID`       | Telegram user ID of bot owner |
| `MAX_VIOLATIONS` | Number of allowed violations before action |
| `LOG_CHANNEL`    | Channel ID to log moderation actions |

---

## 💬 Examples

```bash
✅ /allow @user123      → Allow a user from moderation
❌ /remove @user123     → Remove and re-apply old violations
🔧 /config              → Inline settings panel
📢 /broadcast (reply)   → Send message to all chats
```

---

## 📌 Inline Features

- ⚙️ **Warn Limit**: Increase/decrease per group
- 🔨 **Punishment Type**: Ban, Mute, or Warn Only
- 🔓 **Inline Unmute**: Admins can unmute directly from the warning

---

## 📡 Updates & Support

<p align="center">
  <a href="https://t.me/GrayBots">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://t.me/GrayBotSupport">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

## 🤝 Contributing

We welcome all contributions to improve this bot.

1. 🍴 Fork the repo  
2. 🌿 Create a new branch  
3. 💻 Make your changes  
4. 📥 Commit clearly  
5. 📤 Open a pull request  

For help, ask in our support group.

---

## 📜 License

Licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.
