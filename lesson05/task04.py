'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
import io

import os.path

dict_number = {}
with io.open("text04.txt", encoding='utf-8') as my_file:
    for line in my_file:
        str_number, numb_number = line.split(" — ")
        dict_number[numb_number] = str_number

with open("text04_ru.txt", "w") as my_file:
    for item in dict_number.items():
        if "1" in item[0]:
            my_file.write("Один - " + item[0])
        elif "2" in item[0]:
            my_file.write("Два - " + item[0])
        elif "3" in item[0]:
            my_file.write("Три - " + item[0])
        elif "4" in item[0]:
            my_file.write("Четыре - " + item[0])
