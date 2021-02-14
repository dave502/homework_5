
import os

print('\nЗадание №6 \n******* Учебные предметы *********')

file_name = 'lessons.txt'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)
lessons = dict()

# читаем файл
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # получаем часть строки с часами
        hours = list(line.partition(':')[2])
        # удаляем лишние символы, получаем строку с числами
        hours_str = ''.join(filter(lambda x: x.isdigit() or x == ' ', hours))
        # удаляем лишние символы
        hours_lst = [int(i) for i in hours_str.split()]
        # добавляем значение в словарь
        lessons[line.partition(':')[0]] = sum(hours_lst)

    print(lessons)
