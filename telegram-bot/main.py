import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

# Create a Telegram bot
bot = telegram.Bot('6725664494:AAGxV47zV-ON7aPDOmHTxHqP8uSgQLDVZfo')

# Define a function to greet the user
# def greet_user(update, context):
#     bot.send_message(chat_id=update.message.chat_id, text='Hi there!')

# # Define a function to guide the user through all the commands
# def help_command(update, context):
#     print("sending message user typed start")
#     bot.send_message(chat_id=update.message.chat_id, text='Here are the commands you can use: /start:'
#                                                           ' Start the bot /help: Get help with the '
#                                                           'bot/greet: Greet the '
#                                                           'bot/ask: Ask the bot a question')
#
async def ask_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hello welcome")

# Define a function to respond to the user's selection
# def respond_to_selection(update, context):
#     # Get the user's selection
#     selection = update.message.text
#
#     # Respond to the user's selection
#     if selection == '/greet':
#         bot.send_message(chat_id=update.message.chat_id, text='Hi there!')
#     elif selection == '/ask':
#         bot.send_message(chat_id=update.message.chat_id, text='What would you like to ask?')
#     else:
#         bot.send_message(chat_id=update.message.chat_id, text='Invalid selection.')

# Create an Application object
# Create an Updater object
application = Application.builder().token("6725664494:AAGxV47zV-ON7aPDOmHTxHqP8uSgQLDVZfo").build()

application.add_handler(CommandHandler("start", ask_user))
# application.add_handler(CommandHandler('help', help_command))
# application.add_handler(CommandHandler('greet', greet_user))
#TODO work on these
# application.add_handler(MessageHandler(filters.text, respond_to_selection))

application.run_polling(allowed_updates=Update.ALL_TYPES)