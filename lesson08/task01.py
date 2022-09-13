'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

import time

class ClsDate():
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def get_date(cls, param):  # Метод класса
        p_day, p_month, p_year = param.split("-")
        return int(p_day), int(p_month), int(p_year)
        #print(param)

    @staticmethod
    def validate_date(param):  # Статический метод
        try:
            valid_date = time.strptime(param, '%d-%m-%Y')
            print("Valid date!")
        except ValueError:
            print("Invalid date!")


print(ClsDate.get_date("12-12-2012"))
ClsDate.validate_date("32-12-2012")