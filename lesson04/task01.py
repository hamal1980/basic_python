'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

if len(argv) > 1:
    name_script, production, rate, premium = argv
    production = int(production)
    rate = int(rate)
    premium = int(premium)
    print((production * rate) + premium)
else:
    production = int(input("Введите выработку в часах: "))
    rate = int(input("Введите ставку в часах: "))
    premium = int(input("Введите премию в рублях: "))
    print((production * rate) + premium)

'''
Результат вывода через командную строку:
c:\basic_python\lesson04>python task01.py 10 10 20
120
'''