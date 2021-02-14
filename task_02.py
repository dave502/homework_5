import os

print('\nЗадание №2 \n******** Чтение файла **********')

file_name = 'new_file_with_lines.txt'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)

with open(file_path, 'r') as file:
    lines = file.readlines()
    print(f'В файле {file_name} {len(lines)} строк')
    for i, line in enumerate(lines):
        print(f'В строке №{i+1} количество слов {len(line.split())} ')
