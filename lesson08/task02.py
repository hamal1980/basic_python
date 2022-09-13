'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = float(input("Введите делимое: "))
divider = float(input("Введите делитель: "))

try:
    result = dividend / divider
except ZeroDivisionError:
    raise DivisionZeroException("На ноль делить нельзя!")
else:
    print(f"Корректная операция. Результат: {result}")