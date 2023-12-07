# imports
from flask import Flask, request, Response
from bot_functions import Bot
from messages import replies
import os
from database_handler import UsersDBHandler , MongoDBPYQ , MongoDBNotes


# Enter your telegram bot token here
# https://t.me/test_foundation_iitmbs_bot link for default bot
BOT_TOKEN = os.environ.get(
    "TG_BOT_TOKEN", "6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw"
)

#mongo db url(for testing and dev purpose create ur own db locally or using mongodb atlas and paste the link below)
DB_URL = ""

# insert your webhook url here, you can get it using vscode inbuilt tunneling in ports section
# eg https://01jt23tc-8443.asse.devtunnels.ms/
WEBHOOK_URL = ""


bot = Bot(BOT_TOKEN)
users_db = UsersDBHandler(DB_URL, "foundation", "users")
notes_db = MongoDBNotes(DB_URL, "NOTES", "NOTES")
pyq_db = MongoDBPYQ(DB_URL, "PYQ", "PYQ")
bot.set_webhook(WEBHOOK_URL)
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        response_ = request.get_json()
        chat = bot.validate_update(response_)
        if chat.message_type == "bot_command":
            command = chat.get_command(argument=True)
            if command[0] == "start":
                print("user sent start command")
                #register_user
                if users_db.user_exists(str(response_["message"]["chat"]["id"])):
                    print("user is old")
                    chat.send_message(replies.get("/start_old_user"))
                else:
                    print("user is new")
                    users_db.add_chat_id(str(response_["message"]["chat"]["id"]))
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
                chat.send_inline_keyboard(replies.get("/select"), keyboard)
        return Response("ok", status=200)
    else:
        return "Bot is active now"


if __name__ == "__main__":
    app.run(port=8443, debug=True, use_reloader=True)
    users_db.close_connection()
