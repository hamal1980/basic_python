'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''

class Road:
    def __init__(self, length = 0, width = 0):
        self._length = length
        self._width = width

    def mass_asfalt(self, mass1metr = 25, depth = 5):
        self.mass1metr = mass1metr
        self.depth = depth
        massa = self._length * self._width * self.mass1metr * self.depth / 1000
        return (f"Для дороги длиной {self._length} м, шириной {self._width} м необходимо {massa} т асфальта")

road66 = Road(5000, 20)
print(road66.mass_asfalt(25, 5))