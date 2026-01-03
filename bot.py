import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Bem-vindo ao PepePig Bot!\n\n"
        "/x - Twitter oficial\n"
        "/CA - Contract Address\n"
        "/site - Site oficial\n\n"
        "⚠️ Nunca enviaremos DM. Cuidado com golpes."
    )

async def x_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐦 X (Twitter)\nhttps://x.com/pepepig_crypto"
    )

async def ca_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📄 Contract Address\n0xSEU_CONTRATO_AQUI"
    )

async def site_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Site oficial\nhttps://pepepigcrypto.base44.app/"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("x", x_command))
    app.add_handler(CommandHandler("CA", ca_command))
    app.add_handler(CommandHandler("site", site_command))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()

