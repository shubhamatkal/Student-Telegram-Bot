# imports
from flask import Flask, request, Response
from bot_functions import Bot
import os

"""
if you dont have bot token generated use: 6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw , 
6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM , 
bot link : https://t.me/test_foundation_iitmbs_bot , 
https://t.me/test_main_iitmbs_bot 
but we suggest you to create your own bot token for development 
"""
# Enter your telegram bot token here or set an environment variable named TG_BOT_TOKEN with the bot token
# This will by default take the testing bot token(6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw,
# https://t.me/test_foundation_iitmbs_bot )
BOT_TOKEN = os.environ.get(
    "TG_BOT_TOKEN", "6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw"
)
bot = Bot(BOT_TOKEN)

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
                chat.send_message(replies.get("/start"))
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
# https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/getMe
# https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/setWebhook?url=https://01tt20hz-8443.asse.devtunnels.ms/

if __name__ == "__main__":
    app.run(port=8443, debug=True, use_reloader=True)
