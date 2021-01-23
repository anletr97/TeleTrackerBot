from config import *
import telegram
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from constant import *
from bot_utils import BotUtils


def main():
     """Start the bot."""
     updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
     dispatcher = updater.dispatcher
     # Init bot utils
     bot = BotUtils()
     dispatcher.add_handler(CommandHandler('start', bot.start, pass_args=True))

     #bot.process_schedule()

    # Start the Bot
     updater.start_polling()

    # start_polling() is non-blocking and will stop the bot gracefully.
     updater.idle()

if __name__ == '__main__':
    main()