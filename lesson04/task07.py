'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

from math import factorial


def fact(count: int):
    for i in range(1, count + 1):
        yield factorial(i)



count_fact = input('Пожалуйста, введите количество вычисленных факториалов: ')

try:
    n = int(count_fact)
except ValueError as e:
    print(e)
    exit(1)

for el in fact(n):
        print(el)
