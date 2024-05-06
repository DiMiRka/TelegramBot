from utils import *


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = ('''Для просмотра доступных валют введите команду /values\n
Чтобы начать работу с ботом введите команду боту через пробел в следующем формате:\n 
<имя валюты> \n 
<в какую валюту перевести>\n
<количество переводимой валюты>\n
Пример:\tдоллар евро 24\n
Или введите команду /convert для пошаговой конвертации''')

    bot.reply_to(message, text=text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text=text)


@bot.message_handler(commands=currency)
def autoconvert(message: telebot.types.Message):
    try:
        AutoConverter.auto_covert(message=message)
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}\nВоспользуйтесь командой /help')


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    global auto_conv
    if message.text.isdigit():
        try:
            quote, base, amount, result = AutoConverter.auto_covert(message=message)
        except Exception as e:
            bot.reply_to(message, f'Не удалось обработать команду\n{e}')
        else:
            text = f'{amount} {keys[quote]} равняется {result} {keys[base]}'
            bot.send_message(message.chat.id, text=text)
            auto_conv = []

    else:
        try:
            quote, base, amount, result = Converter.convert(message=message)
        except APIException as e:
            bot.reply_to(message, f'Ошибка пользователя\n{e}')
        except Exception as e:
            bot.reply_to(message, f'Не удалось обработать команду\n{e}')
        else:
            text = f'{amount} {keys[quote]} равняется {result} {keys[base]}'
            bot.send_message(message.chat.id, text=text)


bot.polling(non_stop=True)
