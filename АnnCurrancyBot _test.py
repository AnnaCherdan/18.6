# Выполнила Черданцева Анна. QAP-73.
import telebot
import requests
import json
from config import keys
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.first_name}, я сконвертирую интересующие вас валюты по курсу ЦБР.' \
           f'\nДля этого прошу ввести через пробел:'\
           f'\n<Из какой вылюты> <В какую валюту> <Количество валютных единиц к конвертации>'\
           f'\nСписок доступных валют: /cur'
    print(message.text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def currencies(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
        bot.reply_to(message, text)


bot.polling(none_stop=True)