"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

list_1234 = ["One — 1\n", "Two — 2\n", "Three — 3\n", "Four — 4\n"]
with open("1234.txt", "w") as my_file:
    for line in list_1234:
        my_file.write(line)

replace_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def multiple_replace(target_str, replace_d):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_d.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str


my_f = open("1234.txt", "r")
new_file = open("1234_new.txt", "w")


for line in my_f:
    my_str = multiple_replace(line, replace_dict)
    # print(my_str)
    new_file.write(my_str)

my_f.close()
new_file.close()

"""
Смотрим новый файл
"""
with open("1234_new.txt", "r") as my_new_file:
    print(my_new_file.read())
