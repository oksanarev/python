# 3 Задание.
#. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с
# учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}

class Position(Worker):
    def get_full_name(self):
        get_full_name = " ".join([self.name, self.surname])
        print(f'Ваше полное имя-{get_full_name}')

    def get_total_income(self):
        get_total_income = sum(self._income.values())
        print(f'Ваш полный доход = {get_total_income}руб.')


woker = Position(input('Введите своё имя: \t',),input('Введите свою фамилию: \t'),input('Введите свою должность: \t'),
                 input('Какой у вас оклад? : '),input('А премия? : '))
woker.get_full_name()
woker.get_total_income()

