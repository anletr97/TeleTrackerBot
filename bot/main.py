import telegram
from telegram import Update
from config import BOT_TOKEN, CHAT_ID
from constant import *
from json_utils import JsonUtils
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text(Message.WELCOME)

def help(update: Update, context: CallbackContext):
    update.message.reply_text(Message.HELP, disable_web_page_preview=True, parse_mode='markdown')

def add(update: Update, context: CallbackContext):
    update.message.reply_text(Message.ADD, disable_web_page_preview=True, parse_mode='markdown')

def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    js = JsonUtils()
    txt = update.message.text
    js.add_url(txt)
    update.message.reply_text(update.message.text)

def main():
     """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
     updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
     dispatcher = updater.dispatcher
     dispatcher.add_handler(CommandHandler('start', start))
     # When user sending '/help'
     dispatcher.add_handler(CommandHandler('help', help))
     # When user sending '/add'
     dispatcher.add_handler(CommandHandler('add', add))

     # TODO
     # on noncommand i.e message - echo the message on Telegram
     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    # Start the Bot
     updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
     updater.idle()
# Send message
# def send_msg():
#     try:
#         msg = "This is test message."
#         bot = telegram.Bot(BOT_TOKEN)
#         bot.send_message(chat_id=CHAT_ID, text = msg, parse_mode='Markdown')
#         print("sent")
#     except Exception as ex:
#             print(ex)

# send_msg()
if __name__ == '__main__':
    main()