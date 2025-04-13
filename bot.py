import os
import re

import instaloader
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

loader = instaloader.Instaloader()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me an Instagram Reel link!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    pattern = r"(https?://(www\.)?instagram\.com/(reel|reels)/[A-Za-z0-9_\-]+)"
    match = re.search(pattern, url)

    if match:
        await update.message.reply_text("Downloading...")
        shortcode = match.group(0).split("/")[-1]
        try:
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target="reel")
            for file in os.listdir("reel"):
                if file.endswith(".mp4"):
                    with open(f"reel/{file}", "rb") as video:
                        await update.message.reply_video(video)
                    os.remove(f"reel/{file}")
            os.rmdir("reel")
        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        await update.message.reply_text("Please send a valid Instagram Reel link!")


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
