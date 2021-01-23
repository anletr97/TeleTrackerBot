import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from constant import *
from config import *
import schedule
from file_utils import FileUtils

class BotUtils:
    def __init__(self):
        self.bot = telegram.Bot(BOT_TOKEN)
        pass

    def process_schedule(self, update: Update, context: CallbackContext):
        # message = self.get_message
        print('go')
        while True:
            schedule.every(30).seconds.do(self.send_message, CHAT_ID)

    def get_message(self):
        return "test message"

    def send_message(self, chat_id):
        self.bot.send_message(chat_id, "test")
        print('sent')

    def start(self, update: Update, context: CallbackContext):
        #  update.message.reply_text(Message.WELCOME)
        file = FileUtils()
        arr = file.read(File.NAME)
        for item in arr:
            # msg= Message.get_message(item['pName'], item['pPrice'], item['pImage'])
            name = item['pName']
            price = item['pPrice']
            image = item['pImage']
            msg = Message.get_message(name, price, image)
            update.message.reply_text(msg, parse_mode=telegram.ParseMode.MARKDOWN)
        print('sent')
