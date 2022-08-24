'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    temp = 1
    for el in range(abs(y)):
        temp *= x
    return 1/temp

positiv_number = input("Введите положительное число\n")
try:
    positiv_number = int(positiv_number)
    if positiv_number < 0:
        print("Введено отрицательное число")
        exit(0)
except ValueError:
    print("Ошибка введено не число")
    exit(0)

negative_number = input("Введите отрицательное число\n")
try:
    negative_number = int(negative_number)
    if negative_number > 0:
        print("Введено положительное число")
        exit(0)
except ValueError:
    print("Ошибка введено не число")
    exit(0)

print(f"Опер**: Возвести {positiv_number} в степень {negative_number} =", my_func1(positiv_number, negative_number))

print(f"Цикл: Возвести {positiv_number} в степень {negative_number} =", my_func2(positiv_number, negative_number))