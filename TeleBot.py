import telebot
from config import TOKEN, keys
from utils import APIException, Converter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = ('''Чтобы начать работу с ботом введите команду боту через пробел в следующем формате:\n 
<имя валюты> \n 
<в какую валюту перевести>\n
<количество переводимой валюты>\n
Пример:\tдоллар евро 24\n
Для просмотра доступных валют введите команду /values''')

    bot.reply_to(message, text=text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text=text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        quote, base, amount, result = Converter.convert(message=message)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {keys[quote]} ---> {result} {keys[base]}'
        bot.send_message(message.chat.id, text=text)


bot.polling(non_stop=True)
