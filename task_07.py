import os
import json

print('\nЗадание №7 \n******* Фирмы *********')

file_name = 'firms.txt'
json_file_name = 'firms.json'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)

columns = ['firm', 'form', 'profit', 'loss']
total_profit = 0
profitable_firms = 0
firms_data = []
firms_profits = [{}, {}]

# читаем файл
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # получаем данные из строки в словарь
        firm_data = dict(zip(columns, line.split()))
        # добавляем полученный словарь в общий список словарей фирм
        firms_data.append(firm_data)
        profit = float(firm_data.get('profit')) - float(firm_data.get('loss'))
        # десли есть прибыль - добавляем данне для вычисления средней прибыли
        if profit > 0:
            total_profit += profit
            profitable_firms += 1
        print(f'Прибыль компании {firm_data.get("firm")} составила {profit}')
    print(f'Средняя прибыль компаний составила {total_profit/profitable_firms}')

    # обходим список словарей фирм
    for firm in firms_data:
        firms_profits[0][firm.get('firm')] =int(firm.get('profit')) - int(firm.get('loss'))
    firms_profits[1]['average_profit'] = total_profit/profitable_firms

    print(firms_profits)

# записываем данные в json
with open(os.path.join(desktop, json_file_name), 'w', encoding='utf-8') as json_file:
    json.dump(firms_profits, json_file)

