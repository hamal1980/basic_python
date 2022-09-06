'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Записываем ручкой '{self.title}'")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Рисуем карандашом '{self.title}'")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Подчеркиваем маркером '{self.title}'")

brush1 = Stationery("малярная_кисть")
brush1.draw()

pen1 = Pen("синяя_ручка")
pen1.draw()

pencil1 = Pencil("простой_карандаш")
pencil1.draw()

handle1 = Handle("черный_маркер")
handle1.draw()