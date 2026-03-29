# Moodle Alert System

A Python-based background monitoring tool that scrapes the **SLIIT City Uni Moodle** announcement page and sends real-time updates to you via a **Telegram bot** — so you never miss a Moodle announcement again.

> **Current Version:** v1.6.0

---

## ✨ Features

- 🔍 **Auto-monitoring** — Scrapes the top 3 latest Moodle announcements every 3 hours automatically
- 📩 **Telegram Notifications** — Sends formatted announcement alerts straight to your Telegram
- 🖥️ **Windows Notifications** — Also pops up a desktop notification for each new announcement
- 🤖 **Telegram Bot Commands** — Manually fetch announcements or look up a specific notice on demand
- 🔇 **Silent Background Mode** — Runs with no console window (`.pyw`)
- 💾 **PID Logging** — Saves the process ID to `mas_pid.txt` for easy management
- ⚡ **Auto-install** — `install.py` handles all dependency installation automatically

---

## 📁 Project Structure

```
Moodle-Alert-System/
├── moodle_alert_system.pyw   # Main script — runs silently in background
├── install.py                # Auto-installs required packages
└── LICENSE
```

---

## ⚙️ Requirements

Python 3.x + the following packages (auto-installed by `install.py`):

```
telebot
requests
beautifulsoup4
plyer
```

---

## 🚀 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/ashfaaqrifath/Moodle-Alert-System.git
   cd Moodle-Alert-System
   ```

2. Run the installer to auto-install dependencies:
   ```bash
   python install.py
   ```

3. Open `moodle_alert_system.pyw` and fill in your Telegram credentials in **two places**:
   ```python
   bot_token = "YOUR BOT TOKEN"
   my_chatID = "YOUR CHAT ID"
   ```
   Get these from [@BotFather](https://t.me/botfather) and [@userinfobot](https://t.me/userinfobot).

4. Run the program (silently, no console window):
   ```bash
   pythonw moodle_alert_system.pyw
   ```

The program will start in the background and send a startup Windows notification with its Process ID.

---

## 🤖 Telegram Bot Commands

| Command | Action |
|---------|--------|
| `/start` | Fetch and send the latest 3 Moodle announcements |
| `<notice_id>` | Look up a specific announcement by its Moodle discussion ID (e.g. `12345`) |
| `/stop` | Terminate the program remotely |

---

## ⏱️ How It Works

1. On launch, the program displays a Windows startup notification and logs its PID to `mas_pid.txt`
2. **Thread 1 — Telegram Bot:** Listens for manual commands (`/start`, `/stop`, notice ID lookups)
3. **Main loop — Auto-monitor:** Every **3 hours (10,800 seconds)**, scrapes the SLIIT Moodle VLE and sends the top 3 announcements to Telegram + Windows notifications

Each Telegram message is formatted like:

```
*SITE ANNOUNCEMENT 1 🔴*
*Announcement Title*
_Date & Time_
--------------------------------------------------
Announcement content here...
--------------------------------------------------
[SLIIT Moodle Alert System](link)
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Web Scraping:** `requests`, `BeautifulSoup4`
- **Notifications:** Telegram Bot API (`pytelegrambotapi`), `plyer`
- **Target:** [SLIIT City Uni Moodle VLE](https://vle.sliitcityuni.lk/)

---

## 📄 License

MIT — © Ashfaaq Rifath
