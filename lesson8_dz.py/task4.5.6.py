# 4,5,6 Задания.
#4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

#5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

#6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.

class StoreHouse:
    def __init__(self):
        self._dict = {}

    def reception_st(self, equipment):
        '''
        Добавляем на склад товар
        '''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def transmission_st(self, name):
        '''
        Отгружаем со склада тавар
        '''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, brand, model, price, article):
        self.brand = str(brand)
        self.model = str(model)
        self.price = float(price)
        self.article = str(article)
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.brand},{self.model},{self.price},{self.article}'


class Printer(Equipment):
    def __init__(self, cl_print, brand, model, price, article):
        super().__init__(brand, model, price, article)
        self.cl_print = cl_print


class Scanner(Equipment):

    def __init__(self, image, brand, model, price, article):
        super().__init__(brand, model, price, article)
        self.image = image



class Xerox(Equipment):

    def __init__(self, color_transfer, brand, model, price, article):
        super().__init__(brand, model, price, article)
        self.color_transfer = color_transfer

storhouse = StoreHouse()

scanner = Scanner('цветной', 'Epson', 'DS-1630', 31000, 'A12000')
storhouse.reception_st(scanner)
print(storhouse._dict)
printer = Printer('струйный', 'Panasonic', 'MX-1500', 35000,'S2300')
storhouse.reception_st(printer)
print(storhouse._dict)
xerox = Xerox('цветной', 'Sony','FR-3400', 29000,'N0900')
storhouse.reception_st(xerox)
print(storhouse._dict)
storhouse.transmission_st('Scanner')
print(storhouse._dict)






