'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def amount_cloth(self):
        pass

class Coat(Clothes):
    def __init__(self, name: str, size: float):
        self.size = size
        super().__init__(name)

    @property
    def amount_cloth(self):
        sum = self.size / 6.5 + 0.5
        return sum

class Suit(Clothes):
    def __init__(self, name: str, height: float):
        self.height = height
        super().__init__(name)

    @property
    def amount_cloth(self):
        sum = 2 * self.height + 0.3
        return sum

coat = Coat("Versache", 48)
print(f"Пальто {coat.name} {coat.size} размера потребует {round(coat.amount_cloth)} ткани")

suit = Suit("Dolce&Gabbana", 168)
print(f"Костюм {suit.name} {suit.height} роста потребует {round(suit.amount_cloth)} ткани")