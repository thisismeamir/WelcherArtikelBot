# coding:utf-8
from dotenv import load_dotenv
import os
import telebot
from database import database as db
from Student import student as st

#----- API KEY importing -----
load_dotenv()
__API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(__API_KEY)


#------ Some helper functions -----
def Truepasser(message):
     return True

def messageCreator(word):
     try:
          finalprint = ''
          wordTitle = word[0]['Singular']
          wordTitlelist = wordTitle.split(" ")
          if wordTitlelist[0] == "das":
               icon = "🟡"
          elif wordTitlelist[0] == "die":
               icon = "🔴"
          elif wordTitlelist[0] == "der":
               icon = "🔵"
          
          for i in word:
               pri = f"{i['Name']}:  {i['Singular']}  --  {i['Plural']} \n"
               finalprint += pri
               finalprint  = finalprint
          finalprint = f"{icon} {wordTitle}\n ------\n {finalprint}"
          return finalprint
     except:
          return "Not found"     

#----- BOT body -----
def main():
     # Bot basic commands
     @bot.message_handler(commands=['start'])
     def start(message):
          userid = message.from_user.id
          username = message.from_user.first_name
          username = username.replace(' ', '_')
          userid = str(userid)
          NewStudent = st(username, userid, "A1")
          NewStudent.DatabaseInitialized()
          bot.reply_to(message, f"Hallo ;) \nSchick mir ein Wort.🙂 ")

     @bot.message_handler(commands=['Über'])
     def start(message):
          bot.reply_to(message, "Ich bin ein Bote, Ich hilfe dir mit die Artikel in Deutsch!\n ")

     
     @bot.message_handler(func=Truepasser)
     def wordAsking(message):
          text = message.text
          userid = message.from_user.id
          username = message.from_user.first_name
          username = username.replace(' ', '_')
          userid = str(userid)
          NewStudent = ''
          NewStudent = st(username, userid, "A1")
          NewStudent.DatabaseInitialized()
          word = NewStudent.WordAsked(text)
          send = messageCreator(word)
          bot.reply_to(message, send)     
          #bot.reply_to(message )
         
     bot.polling()
     
if __name__ == '__main__':
     main()




# Bots body
