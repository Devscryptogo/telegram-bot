import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN não encontrado. Defina a variável de ambiente.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐦 X (Twitter)", callback_data="x")],
        [InlineKeyboardButton("📄 Contract Address", callback_data="ca")],
        [InlineKeyboardButton("🌐 Site Oficial", callback_data="website")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_message.reply_text(
        "🚀 *Bem-vindo ao PepePig Bot*\n\n"
        "Clique em um botão abaixo 👇\n\n"
        "⚠️ Nunca enviaremos DM. Cuidado com golpes.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "x":
        await query.message.reply_text(
            "🐦 X (Twitter)\nhttps://x.com/pepepig_crypto"
        )

    elif query.data == "ca":
        await query.message.reply_text(
            "📄 Contract Address\n0xTOKEN_UNDER_CONSTRUCTION"
        )

    elif query.data == "website":
        await query.message.reply_text(
            "🌐 Site Oficial\nhttps://pepepigcrypto.base44.app/"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
