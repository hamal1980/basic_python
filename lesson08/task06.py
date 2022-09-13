'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
class IllegalCount(Exception):
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return f"{self.str} не число!"

class Equipment():
    def __init__(self, name: str, max_papper_format: str):
        self.name = name
        self.max_papper_format = max_papper_format

class Store():
    __stock = dict()
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capasity = capacity
    def __str__(self):
        return f"Склад {self.name} вместимостью {self.capasity} мест"

    def get_equipment(self, equipment: Equipment, count: int):
        try:
            int(count)
        except:
            raise IllegalCount(count)
            exit(0)
        if equipment.name in self.__stock.keys():
            self.__stock[equipment.name] = self.__stock.get(equipment.name) + count
        else:
            self.__stock[equipment.name] = count

    def give_equipment(self, equipment: Equipment, count: int, department: str):
        try:
            int(count)
        except:
            raise IllegalCount(count)
            exit(0)
        if equipment.name in self.__stock.keys():
            #print(self.__stock.get(equipment.name))
            self.__stock[equipment.name] = self.__stock.get(equipment.name) - count
            print(f"Со склада {self.name} передано в отдел {department}  {count} {equipment.name}")
        else:
            print(f"На складе нет ни одного {equipment.name}")

    def return_stock(self):
        return f"На складе {self.name} в настоящий момент кол-во оргтехники: {self.__stock}"


class Printer(Equipment):
    def __init__(self, name, max_papper_format="A4", is_color=True, is_duplex=True, is_mfu=True):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.is_mfu = is_mfu

class Scaner(Equipment):
    def __init__(self, name, max_papper_format="A4", is_color=True, is_duplex=True, resolution=True):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.resolution = resolution

class Scaner(Equipment):
    def __init__(self, name, max_papper_format="A4", is_color=True, is_duplex=True, is_finisher=True):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.is_finisher = is_finisher

sklad = Store("Центральный", 100)
print(sklad)
hp_m428fdn = Printer("HP m428fdn")
sklad.get_equipment(hp_m428fdn, 10)
print(sklad.return_stock())
sklad.give_equipment(hp_m428fdn, 5, "OK")
print(sklad.return_stock())

sklad.get_equipment(hp_m428fdn, "abc")
