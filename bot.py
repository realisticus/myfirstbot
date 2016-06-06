# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Соня, привет!\nБот понимает команды /start, /help и пока что просто отвечает копией присланного ему сообщения")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Тут пока ничего нет")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)