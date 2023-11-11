#imports
import telegram
from telegram import Update ,InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

# Create a Telegram bot
token_main = None
token_foundation = None
token_diploma = None
token_degree = None
token_admin = None

async def ask_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hello welcome , type /selectcourse to select your course")

async def ask_year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Foundation", callback_data="1"),
            InlineKeyboardButton("Diploma", callback_data="2"),
        ],
        [InlineKeyboardButton("Degree", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose your course:", reply_markup=reply_markup)
# Create an Application object
# Create an Updater object
application = Application.builder().token("6725664494:AAGxV47zV-ON7aPDOmHTxHqP8uSgQLDVZfo").build()

application.add_handler(CommandHandler("start", ask_user))
# application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('selectcourse', ask_year))
#TODO work on these
# application.add_handler(MessageHandler(filters.text, respond_to_selection))

application.run_polling(allowed_updates=Update.ALL_TYPES)