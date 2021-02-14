import os

print('\nЗадание №4 \n******* Перевод *********')

file_name = 'file.txt'
new_file_name = 'file_ru.txt'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)
new_file_path = os.path.join(desktop, new_file_name)

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(new_file_path, 'w', encoding='utf-8') as new_file:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # получаем список слов
            words = line.split()
            # если слово есть в словаре - меняем его
            for i, el in enumerate(words):
                if dictionary.get(el):
                    words[i] = dictionary.get(el)
            # записываем строку в новый файл
            new_file.write(" ".join(words).join(' \n'))

