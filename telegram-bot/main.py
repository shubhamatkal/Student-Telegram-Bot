#imports
from flask import Flask, request , Response
import requests
import json

'''
if you dont have bot token generated use: 6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM , 
bot link : https://t.me/test_main_iitmbs_bot 
but we suggest you to create your own bot token for development 
'''
BOT_TOKEN = ""
base_url = f"https://api.telegram.org/bot{BOT_TOKEN}"
#insert your webhook url here, you can get it using vscode inbuilt tunneling in ports section
# eg https://01tt20hz-8443.asse.devtunnels.ms/
WEBHOOK_URL = ""

app = Flask(__name__)

#defining some bot functions
def send_message(chat_id, text ):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {"chat_id":chat_id, "text":text}
    r  = requests.post(url, json=payload)
    return r

def delete_webhook():
    request_url = base_url+'/setWebhook'
    data = {
        'url': ""
    }
    return requests.post(request_url, json=data).json()

def set_webhook( webhook_url: str) -> dict:
    request_url = base_url+'/setWebhook'
    data = {
        'url': webhook_url
    }
    return requests.post(request_url, json=data).json()

delete_webhook()
print("webhook deleted")
set_webhook(WEBHOOK_URL)

@app.route("/" , methods= ['POST', 'GET'])
def index():
    if request.method == 'POST':
        response_ = request.get_json()
        print("RESPONSE")
        print(response_)
        if response_['message']['text'] == "hello":
            send_message(chat_id=response_['message']['chat']['id'],text="this is test" )
        return Response('ok', status= 200)
    else:
      return "this is not post request"


#Notes:
#https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/getMe
#https://api.telegram.org/bot6965083380:AAHDWyCqvIhqYOAhi19gIF7u6CPcQKZ2qPM/setWebhook?url=https://01tt20hz-8443.asse.devtunnels.ms/

if __name__ == '__main__':
    app.run(port=8443, debug=True, use_reloader=False)
