"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

some_strings = ["One two three four\n", "Five six seven\n", "Eight nine\n", "ten\n"]

with open("text.txt", "w") as my_file:
    for line in some_strings:
        my_file.write(line)


with open("text.txt", "r") as my_file:
    some_lines = my_file.readlines()

print(some_lines)

i = 0
words = 0
for line in some_lines:
    i += 1
    words += len(line.split())
    print(f"Кол-во слов в строке {i} - {len(line.split())}")
print(f"Всего строк = {i}")
print(f"Всего слов = {words}")
