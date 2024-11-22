import random
import os
from telebot import TeleBot
import telebot
from token_1 import TOKEN

API_TOKEN = TOKEN
bot = TeleBot(API_TOKEN)

helps_commands = (
    'доступные команды:\n'
    '/mem : выдаёт случайный мем\n'
    '/password : генерирует случайный пароль\n'
    '/utilization : выдаёт информацию о утилизации\n'
)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, helps_commands)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()