import osa


costs_list = list()
currency_list = list()
with open("currencies.txt") as f:
    for line in f:
        s = line.strip().split()
        costs_list.append(s[1])
        currency_list.append(s[2])



def Convert_currency(currency, amount):
    client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?op=ConvertToNum")
    valie_rub = client.service.ConvertToNum(None, currency, 'rub', amount)
    return round(value_rub, 0)


value_rub = list()
for currency, amount in zip(costs_list, currency_list):
    value_rub.append(int(Convert_currency(currency, amount)))

travaling_expenses = sum(value_rub)
print(travaling_expenses)




