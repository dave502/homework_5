
import os
from random import randint

print('\nЗадание №5 \n******* Сумма чисел *********')

file_name = 'digits.txt'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)

# создаём файл
with open(file_path, 'w') as file:
    # записываем количество чисел от 1 до 99
    for i in range(1, randint(1, 100)):
        # записываем число от 1 до 999
        file.write(str(randint(1, 1000))+' ')

# читаем файл и считаем сумму чисел
with open(file_path, 'r') as file:
    digits = [int(i.strip()) for i in file.readline().split()]
    print(sum(digits))
