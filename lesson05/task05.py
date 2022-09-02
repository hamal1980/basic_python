'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint

with open("text05.txt", "w") as my_file:
    for el in range(100):
        my_file.write(str(randint(0, 10))+" ")

with open("text05.txt") as my_file:
    content = my_file.readline()
    list_number = content.split(" ")

sum_number = 0
for el in list_number:
    try:
        sum_number += int(el)
    except:
        continue
print("Сумма чисел равна: ", sum_number)