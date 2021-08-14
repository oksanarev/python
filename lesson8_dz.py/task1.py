# 1 Задание.
#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.


a = input('Введите дату в формате дд-мм-гггг: ')
class Data:
    def __init__(self, day_month_year):
       self.day_month_year = a

    def __str__(self):
        return f'{self.day_month_year}'

    @classmethod
    def my_data(cls, a):
        my_dats = []
        for i in a.split("-"):
            my_dats.append(int(i))
        return my_dats


    @staticmethod
    def vallid(my_dats):
        day, month, year = my_dats[0], my_dats[1], my_dats[2]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1990 <= year <= 2021:
                    print(f'Вы правильно ввели дату!\n{a}')
                else:
                    return print('Неправильно ввели год (1990-2021)')
            else:
                return print('Неправильно ввели месяц')
        else:
            return print('Что это за число?')


data = Data(a)

print(data.__str__())

print(Data.my_data(a))

print(list(map(type, Data.my_data(a))))

Data.vallid(Data.my_data(a))
