'''
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
try:
    number = int(input("Введите число от 0 до 9: "))
except:
    print ('Это не целое число')
    exit(0)
if  0 <= number <=9:
    total = number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number))
    print(f"Число: {total}")
else:
    print("Некорректное число")