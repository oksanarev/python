# 2 Задание.
#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
# уроке знания: реализовать абстрактные классы для основных классов проекта, проверить
# на практике работу декоратора @property.

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def sum_method(self):
        pass

class Clothes(AbstractClass):
    pass
    def sum_method(self):
        return f'Общий расход ткани\t'

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def s_coat(self):
        s_coat = self.V / 6.5 + 0.5
        return round(s_coat)

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def s_suit(self):
        s_suit = self.h * 2 + 0.3
        return round(s_suit)

clothes = Clothes()

coat = Coat(int(input('Введите размер одежды клиента: ')))
suit = Suit(float(input('Введите рост клиента в метрах: ')))
clothes.sum_method()
print(f'На польто пойдёт {coat.s_coat} м. ткани')
print(f'На костюм уйдёт {suit.s_suit} м. ткани')
print(f'{clothes.sum_method()}={coat.s_coat + suit.s_suit} м.')
