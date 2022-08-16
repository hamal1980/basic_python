'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''
try:
    number = int(input("Введите целое положительное число: "))
except:
    print ('Это не целое число')
    exit(0)
if number <= 0:
    print("Число меньше или равно 0")
    exit(0)
rest = -1
while number > 10:
    reminder = number % 10
    number //= 10
    if reminder > rest:
        rest = reminder
print(rest)