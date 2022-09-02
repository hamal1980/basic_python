'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
import io

def is_number(s): #проверка, что в строке записано число
    try:
        float(s)
        return True
    except ValueError:
        return False

with io.open("text03.txt", encoding='utf-8') as my_file:
   list_employer = []
   sum_salary = 0
   count_empl = 0
   for line in my_file:
       name, salary = line.split()
       if is_number(salary):
           sum_salary += float(salary)
           count_empl += 1
       if is_number(salary) and float(salary) < 20000.00:
           list_employer.append(name)
   print("Сотрудники с окладом меньше 20000: ", ", ".join(list_employer))
   print(f"Средняя величина оклада {count_empl} сотрудников: ", round(sum_salary / count_empl, 2))