'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''
def sum_list(list_args):
    result = 0
    for elem in list_args:
        try:
            continue_sum = True # продолжаем суммирование чисел
            result += int(elem)
        except ValueError as e:
            continue_sum = False # заканчиваем суммирование чисел
            break
    return continue_sum, result
sum_total = 0
while True:
    my_list = [str(i) for i in input('Введите целые числа через пробел или  любой символ для выхода \n').split()]
    continue_sum, sum_temp = sum_list(my_list)
    if continue_sum:
        sum_total += sum_temp
        print(sum_total)
    else:
        sum_total += sum_temp
        print(sum_total)
        break

