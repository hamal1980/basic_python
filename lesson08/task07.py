'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    # z1+z2 = a+c+i(b+d)
    def __add__(self, other):
        print(f'Сумма к.числа1 и к.числа2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    # z1*z2 = (ac-bd)+i(ad+cb)
    def __mul__(self, other):
        print(f'Произведение к.числа1 и к.числа2 равно')
        return f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


complex_1 = ComplexNumber(1, -2)
complex_2 = ComplexNumber(3, 4)
print(f"К.число1: {complex_1}")
print(f"К.число2: {complex_2}")
print(complex_1 + complex_2)
print(complex_1 * complex_2)