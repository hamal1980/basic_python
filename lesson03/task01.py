'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
first_number = input("Введите первое число\n")
if first_number.isdigit():
    first_number = int(first_number)
else:
    print("Ошибка введено не число")
    exit(0)

second_number = input("Введите второе число\n")
if second_number.isdigit():
    second_number = int(second_number)
else:
    print("Ошибка введено не число")
    exit(0)

def func_devision(divisible, divisor):
    try:
        return divisible / divisor
    except ZeroDivisionError:
        return f"Ошибка деления"

print(func_devision(first_number, second_number))

