# Insta-to-Video TB Bot

A Telegram bot that downloads Instagram Reels and forwards them into your Telegram chat or channel.  
Built with Python

---

## 🚀 Features

- **Reel detection**: accepts any Instagram URL of type `/reel/`, `/reels/`, or `/p/`  
- **Automated download**: grabs the MP4 file via Instaloader  
- **Telegram delivery**: sends the downloaded video back to the user  
- **Error handling**: notifies on invalid URLs or download failures  
- **Cleanup**: removes temporary files after sending  

---

## 🛠️ Prerequisites

- **Python** ≥ 3.8  
- **Telegram Bot token** (from [@BotFather](https://t.me/BotFather))  
- **FFmpeg** installed on your system (optional, only if you later add video processing)  
- **Python dependencies** (see **Dependencies** below)  

---

## ⚙️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/insta-to-video-tb-bot.git
   cd insta-to-video-tb-bot
   ```

2. **(Optional) Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your bot token**  
   - Copy the example environment file:  
     ```bash
     cp .env.example .env
     ```  
   - Open `.env` and set your Telegram token:  
     ```
     BOT_TOKEN=123456789:ABCdefGhIJK_lMnopQRsTuvWxYz
     ```

---

## 🖥️ Usage

1. **Start the bot**  
   ```bash
   python bot.py
   ```

2. **Interact**  
   - Send `/start` to receive a welcome message.  
   - Send an Instagram Reel URL (e.g. `https://www.instagram.com/reel/CabcdEFGhIj/`).  
   - The bot replies “Downloading…”, then sends you the `.mp4` file.

---

## 📂 Project Structure

```
insta-to-video-tb-bot/
├── bot.py               # Main bot script
├── requirements.txt     # Python dependencies
├── .env.example         # Sample environment variables
└── reel/                # Temporary download folder
```

- **bot.py**  
  - Loads `BOT_TOKEN` from `.env`  
  - Defines `/start` and text handlers  
  - Uses a regex to validate Instagram Reel URLs  
  - Downloads via Instaloader, sends via Telegram, then cleans up  

---

## ⚙️ Dependencies

Listed in `requirements.txt`:

```
python-dotenv
instaloader
python-telegram-bot>=20.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📄 License

Distributed under the MIT License. See the [LICENSE](./LICENSE) file for details.
