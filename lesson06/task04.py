'''
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, name, speed, color, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print(f"Машина {self.name} поехала")
    def stop(self):
        print(f"Машина {self.name} остановилась")
    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")
    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed}")

class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def show_speed(self):
        if self.speed <= 60:
            print(f"Скорость машины {self.name}: {self.speed}")
        else:
            print(f"Скорость машины {self.name} превышена!")

class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def show_speed(self):
        if self.speed <= 40:
            print(f"Скорость машины {self.name}: {self.speed}")
        else:
            print(f"Скорость машины {self.name} превышена!")

class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

police_car = PoliceCar("police car 911", 100, "red", True)
police_car.go()
police_car.stop()
police_car.turn("налево")
police_car.show_speed()


town_car1 = TownCar("town_car_1", 61, "black", False)
print(f"Машина {town_car1.name} цвета {town_car1.color} ехала со скоростью {town_car1.speed}. Отношение к полиции {town_car1.is_police}")
town_car1.go()
town_car1.show_speed()