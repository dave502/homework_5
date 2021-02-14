import os

print('\nЗадание №1 \n******** Создание файла **********')
# создаём файл на рабочем столе
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, 'new_file_with_lines.txt')

with open(file_path, 'w') as new_file:
    while True:
        new_line = input('Введите строку: ')
        if new_line:
            new_file.write(new_line + '\n')
        else:
            print(f'Создан файл {file_path}')
            break
