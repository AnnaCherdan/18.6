import requests
import json
from config import keys


class APIException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'конвертируемые валюты должны быть различны.'\
                               f' Я не могу перевести валюту в саму себя!')
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
        # try:
        #     isinstance(base_ticker, str)
        # except KeyError:
        #     raise APIException(f'вводим буковки')
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException(f'я отрицательные значения конвертировать не умею!')
        except ValueError:
            raise APIException(f'количество надо вводить в виде числового значения.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
