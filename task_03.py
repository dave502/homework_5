
import os

print('\nЗадание №3 \n***** Зарплаты сотрудников *******')

file_name = 'new_file_with_lines.txt'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, file_name)

# список данных по сотрудникам
salary_table = [(1, 'Иванов', 15000), (2, 'Петров', 19555), (3, 'Сидоров', 25000),
                (4, 'Сергеев', 25000), (5, 'Андреев', 23000)]

# запись данных по сотрудникам в файл в виде таблички
with open(file_path, 'r+') as file:
    for line in salary_table:
        file.write(f'{line[0]:2}|{line[1]:^20}|{line[2]:10}\n')

# чтение данных по сотрудникам из файла
columns = ['№', 'employee', 'salary']
with open(file_path, 'r') as file:
    total_salaries = 0
    # Сотрудники с зарплатой меньше 20 000 руб
    employees_list = []
    # получаем список строк
    salaries = file.readlines()
    # для каждой строки получаем список данных
    for salary_str in salaries:
        # список [ №, сотрудник, зарплата ]
        salary_line = [i.strip() for i in salary_str.split('|')]
        # словарь [ '№':№, 'employee':сотрудник, 'salary':зарплата]
        # для удобства доступа к данным
        salary_dict = dict(zip(columns, salary_line))
        # вывод фамилии сотрудников с з/п < 20 000
        if int(salary_dict.get('salary')) < 20000:
            employees_list.append(salary_dict.get('employee'))

        # суммируем з/п
        total_salaries += int(salary_dict.get('salary'))

    if len(salaries):
        print(f'Средняя зарплата сотрудников = {total_salaries/len(salaries):.3f}')

    if len(employees_list):
        print(f'Сотрудники с зарплатой меньше 20 000 руб.: {employees_list}')
