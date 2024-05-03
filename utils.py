import telebot
import requests
from config import keys, apikey


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(message: telebot.types.Message):
        val = message.text.split(' ')

        if len(val) > 3:
            raise APIException('Вы ввели больше 3-х параметров конвертации')

        if len(val) < 3:
            raise APIException('Вы ввели меньше 3-х параметров конвертации')

        quote, base, amount = val
        quote, base = quote.lower(), base.lower()

        if quote == base:
            raise APIException('Невозможно конвертировать одинаковые валюты')

        if quote not in keys.keys():
            raise APIException(f'Валюта "{quote}" для конвертации не обрабатывается')

        if base not in keys.keys():
            raise APIException(f'Валюта "{base}" для конвертации не обрабатывается')

        if not amount.isdigit():
            raise APIException('Третьим параметром введите целое число')

        a = requests.get(
            url=f'https://api.apilayer.com/fixer/convert?to={keys[base]}&from={keys[quote]}&amount={con_sum}',
            headers=apikey).json()
        result = a.get('result')
        return quote, base, amount, result
