#imports
from flask import Flask, request , Response
import requests
import json
from bot_functions import Bot
from messages import replies
'''
if you dont have bot token generated use: 6677627030:AAElX2DcR0vWqDGHdgbTio9og1DLJiMK5Mw , 
6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM , 
bot link : https://t.me/test_foundation_iitmbs_bot , 
https://t.me/test_main_iitmbs_bot 
but we suggest you to create your own bot token for development 
'''
BOT_TOKEN = ""
bot = Bot(BOT_TOKEN)
#insert your webhook url here, you can get it using vscode inbuilt tunneling in ports section
# eg https://01jt23tc-8443.asse.devtunnels.ms/
WEBHOOK_URL = ""

app = Flask(__name__)

bot.set_webhook(WEBHOOK_URL)

@app.route("/" , methods= ['POST', 'GET'])
def index():
    if request.method == 'POST':
        response_ = request.get_json()
        # test_ = bot.validate_update(response_)
        if response_['message']['text'] == "/start":
            bot.send_message(chat_id=response_['message']['chat']['id'],text=replies["/start"] )
        if response_['message']['text'] == "/select":
            bot.send_message(chat_id=response_['message']['chat']['id'],text=replies["/select"] )
        return Response('ok', status= 200)
    else:
        return 'Bot is active now'


#Notes:
#https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/getMe
#https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/setWebhook?url=https://01tt20hz-8443.asse.devtunnels.ms/

if __name__ == '__main__':
    app.run(port=8443, debug=True, use_reloader=True)
