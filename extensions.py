import requests
import json
from config import keys


class APIException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == amount:
            raise APIException(f'название валюты надо вводить буквами, как в образце. /help')
        elif base == amount:
            raise APIException(f'название валюты надо вводить буквами, как в образце. /help')
        elif quote == base:
            raise APIException(f'конвертируемые валюты должны быть различны.'\
                               f' Я не могу перевести валюту в саму себя! /help')
        elif quote not in keys:
            raise APIException(f'данной валюты "{quote}" нет в списке доступных валют. Проверьте, пожалуйста,'\
                               f' написание.  /values')
        elif base not in keys:
            raise APIException(f'данной валюты "{base}" нет в списке доступных валют. Проверьте, пожалуйста,'\
                               f'написание. /values')
        else:
            ...
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'вводить название "{quote}" надо с большой буквы, как в образце.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'вводить название "{base}" надо с большой буквы, как в образце.')
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException(f'я отрицательные значения или ноль конвертировать не умею! /help')
        except ValueError:
            raise APIException(f'"Количество" надо вводить в виде числового значения. /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
