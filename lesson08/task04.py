'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

class Store():
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capasity = capacity
    def __str__(self):
        return f"Склад {self.name} вместимостью {self.capasity} мест"

class Equipment():
    def __init__(self, name: str, max_papper_format: str):
        self.name = name
        self.max_papper_format = max_papper_format

class Printer(Equipment):
    def __init__(self, name, max_papper_format, is_color: bool, is_duplex: bool, is_mfu: bool):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.is_mfu = is_mfu

class Scaner(Equipment):
    def __init__(self, name, max_papper_format, is_color: bool, is_duplex: bool, resolution: bool):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.resolution = resolution

class Scaner(Equipment):
    def __init__(self, name, max_papper_format, is_color: bool, is_duplex: bool, is_finisher: bool):
        super().__init__(name, max_papper_format)
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.is_finisher = is_finisher