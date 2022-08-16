'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
sec = int(input("Введите время в секундах: "))
if sec < 60:
    hours = 0
    mins = 0
    secs = sec
    print(f"Время: {hours:02}:{mins:02}:50{secs:02}")
elif 60 <= sec < 3600:
    hours = 0
    mins = sec // 60
    secs = sec % 60
    print(f"Время: {hours:02}:{mins:02}:{secs:02}")
elif sec >= 3600:
    hours = sec // 3600
    mins = (sec - hours * 3600) // 60
    secs = (sec - hours * 3600) % 60
    print(f"Время: {hours:02}:{mins:02}:{secs:02}")
else:
    print("Некорректное значение")
