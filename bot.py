# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

def shm_word(word):
    is_first_capital = word[0].isupper()
    word = word.lower()
    vowels = ['а','о','у','ы','е','э','я','и','ю', 'ё']
    try:
        first_vowel = min(word.find(vowel) for vowel in vowels if vowel in word)
        word = 'шм' + word[first_vowel:]
    except ValueError:
        word = 'шм' + word[2:]

    if is_first_capital:
        word = word.title()
    return word

def shm_text(text):
    return ' '.join(filter(None, map(shm_word, text.split())))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет!\nБот понимает команды /start, /help и пока что просто проказничает с вашими сообщениями")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Тут ничего нет, пыщь пыщь")

@bot.message_handler(content_types=["text"])
def sh_message(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, shm_text(message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True)