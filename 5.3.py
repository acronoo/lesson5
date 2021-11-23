"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

import random

employers = ["Иванов", "Петров", "Сидоров", "Смирнов", "Орлов", "Лермонтов", "Пушкин", "Гоголь", "Толстой",
             "Маяковский"]

with open("salaries.txt", "w") as my_file:
    for worker in employers:
        my_file.write(f"{worker} {random.uniform(10000, 30000)}\n")

with open("salaries.txt", "r") as my_file:
    content = my_file.readlines()

print(content)

i = 0  # Считаем кол-во строк (сотрудников)
sum_salary = 0  # Считаем сумарный доход всех работников
for line in content:
    i += 1
    x, y = line.split()
    # print("x = ", x)
    # print("y = ", y)
    if float(y) < 20000:
        print(f"У работника {x} оклад менее 20000. Его оклад = {y}")
    sum_salary += float(y)
print(f"Сумарный доход всех сотрудников = {sum_salary}")
print(f"Всего сотрудников = {i}")
print(f"Средний доход сотрудников составляет {sum_salary / i}")