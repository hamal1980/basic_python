'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open("text01.txt") as my_file:
    count_lines = 0
    for line in my_file:
        count_lines += 1
        print(f"Количество слов в {count_lines} строке", len(line.split()))
    print("Число строк в файле: ", count_lines)