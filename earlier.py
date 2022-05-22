# Выполнила Черданцева Анна. QAP-73.
# https://min-api.cryptocompare.com/data/price?fsym=ЧЕГО&tsyms=ВОЧТО
import telebot
import requests
import json
from config import keys
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


class ConvertionException(Exception):
    pass


@bot.message_handler(commands=['start', 'help'])
def welcome(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.first_name}, я сконвертирую интересующие вас валюты.' \
           f'\nДля этого прошу ввести через пробел:'\
           f'\n<Из какой вылюты> <В какую валюту> <Количество валютных единиц к конвертации>'\
           f'\nСписок доступных валют: /values'
    print(message.text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) > 3:
        raise ConvertionException('Вы ввели лишние значения.')
    elif len(values) < 3:
        raise ConvertionException('Вы не ввели необходимые значения или пропустили пробел.')
    quote, base, amount = values
    quote_ticker, base_ticker = keys[quote], keys[base]
    if quote == base:
        raise ConvertionException(f'Конвертируемые валюты должны быть различны.'\
         f'Я не могу перевести валюту в саму себя!')
    else:
        ...

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Данные по конвертации {quote} отсутствуют.')
    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Данные по конвертации {base} отсутствуют.')

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Итог конвертации: {amount} {quote} в {base} составит {total_base}.'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)