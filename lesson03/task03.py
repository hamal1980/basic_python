'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
arg1 = 6
arg2 = 5
arg3 = 2
def my_func(var1, var2, var3):
    if var2 > var1 < var3: # меньшее var1
        return var2 + var3
    elif var1 > var2 < var3: #меньшее var2
        return var1 + var3
    elif var1 > var3 < var2: #меньшее var3
        return var1 + var2
    else:                   #все числа равны
        return 2 * var1

print(my_func(arg1, arg2, arg3))