
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEAGRAM_BOT_TOKEN", None)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CaOps bot online. Use /watch <topic|token|@channel>")

async def watch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /watch <topic|token|@channel>")
        return
    topic = " ".join(args)
    await update.message.reply_text(f"Started watching (demo): {topic}")

def run_bot():
    if not TOKEN:
        print("No TELEGRAM_BOT_TOKEN set — bot is disabled (dry-run mode).")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("watch", watch))
    app.run_polling()
