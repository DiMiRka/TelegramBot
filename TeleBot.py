import telebot

TOKEN = "6401568675:AAE0Rq0Z4oA_6y8E5RBpzbdYmtaKGcuZ0Ls"

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

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


bot.polling(non_stop=True)
