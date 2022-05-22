import telebot
from config import keys, TOKEN
from extensions import APIException, CriptoConverter

bot = telebot.TeleBot(TOKEN)


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
    try:
        values = message.text.split(' ')
        if len(values) > 3:
            raise APIException('вы ввели лишние значения.')
        elif len(values) < 3:
            raise APIException('вы не ввели три необходимых значения, пропустили пробел.')
        else:
            quote, base, amount = values
            total_base = CriptoConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Я не смог сконвертировать, потому что \n{e}')
    # except Exception as e:
    #     bot.reply_to(message, f'Не удалось обработать коменду\n{e}')
    else:
        text = f'Итог: {amount} {quote} конвертируем(а) в {base} в размере {total_base} у.е.'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)