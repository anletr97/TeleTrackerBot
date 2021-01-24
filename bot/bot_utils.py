"""This module will process telegram bot method"""
import schedule
import telegram
from telegram import Update
from telegram.ext import CallbackContext
from constant import File, Message
from config import BOT_TOKEN, CHAT_ID
from file_utils import FileUtils

class BotUtils:
    '''Handle bot's job'''
    def __init__(self):
        self.bot = telegram.Bot(BOT_TOKEN)

    def process_schedule(self):
        '''Schedule for send message process'''
        # message = self.get_message
        print('go')
        while True:
            schedule.every(30).seconds.do(self.send_message, CHAT_ID)

    def send_message(self, chat_id):
        '''Handle sending message'''
        self.bot.send_message(chat_id, "test")
        print('sent')

    def start(self, update: Update, context: CallbackContext):
        '''Process when people enter /start'''
        #  update.message.reply_text(Message.WELCOME)
        file = FileUtils()
        arr = file.read(File.NAME)
        print(context)
        for item in arr:
            # msg= Message.get_message(item['pName'], item['pPrice'], item['pImage'])
            name = item['pName']
            price = item['pPrice']
            image = item['pImage']
            msg = Message().get_message(name, price, image)
            update.message.reply_text(msg, parse_mode=telegram.ParseMode.MARKDOWN)
        print('sent')
