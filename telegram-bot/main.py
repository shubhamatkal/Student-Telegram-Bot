# imports
from flask import Flask, request, Response
from bot_functions import Bot
import os
from database_handler import UserDataManager

# Enter your telegram bot token here or set an environment variable named TG_BOT_TOKEN with the bot token
# This will by default take the testing bot token(6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw,
# https://t.me/test_foundation_iitmbs_bot )
BOT_TOKEN = os.environ.get(
    "TG_BOT_TOKEN", "6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw"
)
bot = Bot(BOT_TOKEN)

#mongo db url(for testing and dev purpose create ur own db locally or using mongodb atlas and paste the link below)
DB_URL = ""

db = MongoDBHandler(DB_URL, "iitm-bot", "users")

# insert your webhook url here, you can get it using vscode inbuilt tunneling in ports section
# eg https://01jt23tc-8443.asse.devtunnels.ms/
WEBHOOK_URL = ""

app = Flask(__name__)

bot.set_webhook(WEBHOOK_URL)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        response_ = request.get_json()
        chat = bot.validate_update(response_)
        if chat.message_type == "bot_command":
            command = chat.get_command(argument=True)
            if command[0] == "start":
                #register_user
                if db.is_chat_id_exist(response_["message"]["chat"]["id"]):
                    chat.send_message(replies.get("/start_old_user"))
                else:
                    db.register_chat_id(response_["message"]["chat"]["id"])
                    chat.send_message(replies.get("/start_new_user"))
            elif command[0] == "select":
                keyboard = {
                    "inline_keyboard": [
                        [bot.callback_button("Foundation", "1")],
                        [
                            bot.callback_button("Diploma Programming", "2"),
                            bot.callback_button("Diploma DS", "3"),
                        ],
                        [bot.callback_button("Degree", "4")],
                    ]
                }
                chat.send_inline_keyboard(replies["commands"].get("select"), keyboard)
        return Response("ok", status=200)
    else:
        return "Bot is active now"


# Notes:
# Add chat_ids
# mongo_handler.add_chat_id("Bob")
# # Add subjects to a specific user
# mongo_handler.add_subjects_to_user("Shubham", ["Math", "Science"])
# mongo_handler.add_subjects_to_user("Bob", ["History", "Geography"])


if __name__ == "__main__":
    app.run(port=8443, debug=True, use_reloader=True)
    db.close_connection()