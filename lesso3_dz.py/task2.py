# 2 задание.
def user (name, sur_name, year, city, email, tel):
    return print(f"Ваши данные - {name}, {sur_name};год рождения - {year};место рождения -{city};Email -{email};телефон - {tel}")
a = input("Введите ваше имя: ")
b = input("Введите свою фамилию: ")
c = int(input("Введите год рождения: "))
d = input("Введите место рождения: ")
e = input( "Ваш email: ")
f = input("Ваш телефон: ")

user(name=a, sur_name=b, year=c, city=d, email=e, tel=f)

