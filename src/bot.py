from dotenv import load_dotenv
import os
import telebot
from core.objects import database as db

#----- API KEY importing -----
load_dotenv()
__API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(__API_KEY)

#----- BOT body -----
def main():
     @bot.message_handler(commands=['start'])
     def start(message):
          # Here should be some initializing, database adding and timer starting codes
          print("Someone Started")
          bot.reply_to(message, "Welcome")
     bot.infinity_polling()          

if __name__ == '__main__':
     main()


