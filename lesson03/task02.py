'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


# именованные параметры
#def second_func(var_2, var_1, var_3):
#    print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")
#
#
#second_func(var_1=10, var_2=20, var_3=30)

def user_data(name, surname, birtday, city, email, phone):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {birtday}, Город проживания: {city}, email: {email}, Телефон {phone}")

user_data(name="Степан", phone="8923541123", surname="Кузнецов", birtday="1990", city="Москва", email="stepaky@gmial.com")