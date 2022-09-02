'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''
import json

profit_company = {}
average_profit = {}
sum_profit = 0
i = 0

with open("text07.txt") as my_file:
    for line in my_file:
        firm, type_company, revenue, costs = line.split(" ")
        profit = float(revenue) - float(costs)
        if profit > 0:
            sum_profit += profit
            i += 1
        profit_company[firm] = abs(profit)
    average_profit["average_profit"] = sum_profit / i
company_list = (profit_company, average_profit)
print("Итоговый список: ", company_list)

with open("text07.json", "w") as my_file:
    json.dump(company_list, my_file)
    json_str = json.dumps(company_list)
    print("Содержимое json файла:", json_str)