# Выполнила Черданцева Анна. QAP-73.
# https://min-api.cryptocompare.com/data/price?fsym=ЧЕГО&tsyms=ВОЧТО
import telebot
import requests
import json
from config import keys
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


# class ConvertionException(Exception):
#     pass
#
#
# class CriptoConverter:
#     @staticmethod
#     def convert(quote: str, base: str, amount: str):
#         # quote, base, amount = values
#         # values = message.text.split(' ')
#         quote_ticker, base_ticker = keys[quote], keys[base]
#         r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
#         values = message.text.split(' ')
#         total_base = json.loads(r.content)[keys[base]]
#         if len(values) > 3:
#             raise ConvertionException('Вы ввели лишние значения.')
#             # bot.reply_to(message, ConvertionException)
#         else:
#             ...
#         if len(values) < 3:
#             raise ConvertionException('Вы не ввели необходимые значения или пропустили пробел.')
#         else:
#             ...
#
#         if quote == base:
#             raise ConvertionException(f'Конвертируемые валюты должны быть различны.' \
#                                       f'Я не могу перевести валюту в саму себя!')
#         else:
#             ...
#         try:
#             quote_ticker = keys[quote]
#         except KeyError:
#             raise ConvertionException(f'Данные по конвертации {quote} отсутствуют.')
#         try:
#             base_ticker = keys[base]
#         except KeyError:
#             raise ConvertionException(f'Данные по конвертации {base} отсутствуют.')
#         try:
#             amount = float[amount]
#         except ValueError:
#             raise ConvertionException(f'Данное значение количества, {amount}, конвертации не подлежит.')


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
    quote, base, amount = values
    # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = CriptoConverter.convert(quote, base, amount)
    # total_base = json.loads(r.content)[keys[base]] * amount
    text = f'Итог: {amount} {quote} конвертируем в {base} в размере {total_base}.'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

