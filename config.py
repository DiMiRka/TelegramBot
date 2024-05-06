TOKEN = "6401568675:AAE0Rq0Z4oA_6y8E5RBpzbdYmtaKGcuZ0Ls"
keys = {
    'Доллар': 'USD',
    'Евро': 'EUR',
    'Рубль': 'RUB',
    'Фунт': 'GBP',
    'Иена': 'JPY',
    'Франк': 'CHF',
    'Юань': 'CNY'
}
con_keys = keys.copy()
auto_conv = []
counter = 0
currency = ('convert,' + ','.join(keys.keys())).split(',')
apikey = {'apikey': 'CpNPLsHLH3OBTXZ9ZISVNMGAJMnfOqeV'}
