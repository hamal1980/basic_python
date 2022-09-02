'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import io

def return_number(my_str):
    num = ''
    for char in my_str:
        if char.isdigit():
            num = num + char

    if num != '':
        return int(num)
    else:
        return 0

with io.open("text06.txt", encoding='utf-8') as my_file:
    ed_list = {}
    for line in my_file:
        subject, ed_hours = line.split(": ")
        lect, pr, lab = ed_hours.split(" ")
        sum_ed = return_number(lect) + return_number(pr) + return_number(lab)
        ed_list[subject] = sum_ed
    print(ed_list)

