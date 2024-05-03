keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}


def convert():
    val = input('Конвертация').split(' ')
    con_1, con_2, con_sum = val
    con_1, con_2 = con_1.lower(), con_2.lower()

    if con_1 not in keys.keys():
         return print(f'Валюта "{con_1}" для конвертации не обрабатывается')

    if con_2 not in keys.keys():
        return print(f'Валюта "{con_2}" для конвертации не обрабатывается')

    if not con_sum.isdigit():
        return print('Третьим параметром введите целое число')

    print(f'{con_1} в {con_2} кол {con_sum}')


convert()