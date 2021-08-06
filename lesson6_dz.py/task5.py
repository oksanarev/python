# 5 Задание.
#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
#  класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
#  из классов реализовать переопределение метода draw. Для каждого из
#  классов методы должен выводить уникальное сообщение. Создать экземпляры
#  классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title =  title

    def draw(self):
        return f'Запуск отрисовки. \t'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} проводит тонкую линию. \t'

class Pensil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} ресует тонкую линию. \t'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} проводит жирную полосу. \t'

stationery = Stationery('Канцтовар')
pen = Pen('Ручка')
pensil = Pensil('Карандаш')
handle = Handle('Маркер')
print(stationery.draw())
print(pen.draw())
print(pensil.draw())
print(handle.draw())