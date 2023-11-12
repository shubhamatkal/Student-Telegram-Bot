#imports
from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes
import os

# Get telegram bot tokens from local variables
#replace P_TEL_.... with your name of local var for token
TOKEN_MAIN = os.environ.get("P_TEL_MAIN")


#defining some funtions
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
main_bot = Application.builder().token(TOKEN_MAIN).build()


#creating handlers
main_bot.add_handler(CommandHandler("start", ask_user))


# application.add_handler(CommandHandler('help', help_command))
main_bot.add_handler(CommandHandler('selectcourse', ask_year))



#polling
main_bot.run_polling(allowed_updates=Update.ALL_TYPES)

