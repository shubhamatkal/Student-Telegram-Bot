# Basic Telegram Bot Api Support for python
This is a very simple Telegram Bot API support for python.

## Basic Usage
```python
from bot_functions import Bot
bot = Bot() # This will use environment TG_BOT_TOKEN for token
BOT_TOKEN = '123456:Qtjyq9uieyyfwltyfdeoslfge'
bot = Bot(BOT_TOKEN) # This will use the value of BOT_TOKEN for token 

# Sending messages to an user
sent = bot.send_message(chat_id, text)

# Editing sent message
sent.edit_message_text(new_text)
# Another way
bot.edit_message_text(chat_id, message_id, new_text)

# deleting sent message
sent.delete_message()
# Another way
bot.delete_message(chat_id, message_id)
```

## All available methods and properties
- `PARSE_MODES` :
    * `PARSE_MODES.HTML` - HTML parse mode 
    * `PARSE_MODES.MD` - Markdown parse mode
- `set_webhook()` : Set webhook for your bot\
Usage: `bot.set_webhook(webhook_url)`
- `sent_message()` : visit [official telegram bot api documentation](https://core.telegram.org/bots/api#sendmessage).
- `edit_message_text()` : visit [official telegram bot api documentation](https://core.telegram.org/bots/api#editmessagetext).
- `delete_message()`: Usage `bot.delete_message(chat_id, message_id)`

**I'll Update The Documentation After Completeing This Basic Bot Class**

**PLEASE NOTE: THIS BOT CLASS USES SYNC CODE EXECUTION SO IT MIGHT BE A LITTLE SLOW, YOU CAN USE THREADING TO BOOST PERFORMANCE, I'M PLANNING TO ADD ASYNC SUPPORT FOR NEXT VERSION**