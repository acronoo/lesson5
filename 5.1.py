"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

user_input = "."
out_f = open("data.txt", "w+")
while user_input != "":
    user_input = input("Введите строку, которую необходимо записать в файл. "
                       "Для выхода из программы просто нажмите enter: ")
    out_f.write(user_input + "\n")

out_f.close()

with open("data.txt") as my_file:
    print(my_file.read())
