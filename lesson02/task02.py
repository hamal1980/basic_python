'''
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
'''

my_list = [str(i) for i in input('Введите значения списка через пробел ').split()]
print(my_list)
index_el = 1 #счетчик для индекса списка
for el in my_list:
    if index_el % 2:
        temp_val = el
        index_el += 1
    else:
        my_list[index_el - 2] = my_list[index_el-1]
        my_list[index_el-1] = temp_val
        index_el += 1
print(my_list)