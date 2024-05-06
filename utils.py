import telebot
from telebot import types
import requests
from config import *

bot = telebot.TeleBot(TOKEN)


class APIException(Exception):
    pass


class AutoConverter:
    @staticmethod
    def auto_covert(message: telebot.types.Message):
        global counter, con_keys, auto_conv
        if message.text == '/convert':
            auto_conv = []
            counter = 0

        if counter == 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for key in keys.keys():
                markup.add('/'.join(('', key)))
            bot.send_message(message.chat.id, text='Выберите валюту, которую будите конвертировать:',
                             reply_markup=markup)
            counter += 1
            return False
        elif counter == 1:
            auto_conv.append(message.text.replace('/', ''))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            con_keys.pop(message.text.replace('/', ''))
            for key in con_keys.keys():
                markup.add('/'.join(('', key)))
            bot.send_message(message.chat.id, text='Выберите валюту для конвертации:', reply_markup=markup)
            counter += 1
            con_keys = keys.copy()
            return False
        elif counter == 2:
            auto_conv.append(message.text.replace('/', ''))
            bot.send_message(message.chat.id, text='Введите количество переводимой валюты',
                             reply_markup=types.ReplyKeyboardRemove())
            counter += 1
            return False
        else:
            auto_conv.append(message.text)
            quote, base, amount = auto_conv
            a = requests.get(
                url=f'https://api.apilayer.com/fixer/convert?to={keys[base]}&from={keys[quote]}&amount={amount}',
                headers=apikey).json()
            result = str(round(float(a.get('result')), 2))
            counter = 0
            return quote, base, amount, result


class Converter:
    @staticmethod
    def convert(message: telebot.types.Message):
        val = message.text.split(' ')

        if len(val) > 3:
            raise APIException('Вы ввели больше 3-х параметров конвертации\nВоспользуйтесь командой /help')

        if len(val) < 3:
            if auto_conv:
                raise APIException(f'Для конвертации {auto_conv[0]} в {auto_conv[1]} введите целое число для конвертации')
            else:
                raise APIException('Вы ввели меньше 3-х параметров конвертации\nВоспользуйтесь командой /help')

        quote, base, amount = val
        quote, base = quote.lower(), base.lower()
        quote, base = quote.capitalize(), base.capitalize()

        if quote == base:
            raise APIException('Невозможно конвертировать одинаковые валюты\nВоспользуйтесь командой /help')

        if quote not in keys.keys():
            raise APIException(f'Валюта "{quote}" для конвертации не обрабатывается\nВоспользуйтесь командой /help')

        if base not in keys.keys():
            raise APIException(f'Валюта "{base}" для конвертации не обрабатывается\nВоспользуйтесь командой /help')

        if not amount.isdigit():
            raise APIException('Третьим параметром введите количество для конвертации в виде целого числа\nВоспользуйтесь командой /help')

        a = requests.get(
            url=f'https://api.apilayer.com/fixer/convert?to={keys[base]}&from={keys[quote]}&amount={amount}',
            headers=apikey).json()
        result = str(round(float(a.get('result')), 2))
        return quote, base, amount, result
