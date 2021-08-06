# 4. Задание.
#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

direction = ['left', 'right']
class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехала\t'

    def stop(self):
        return f"{self.name} остановилась\t"

    def turn(self, direction):
        if direction == 'left':
            return f'{self.name} повернула на лево\t'
        else:
            return f'{self.name} повернула на право\t'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):

        if self.speed <= 60:
            return f'У {self.name} допустимая скорость.\t'
        else:
            return f'{self.name} привышает скорость!\t'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WokerCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed <= 40:
            return f'У {self.name} допустимая скорость.\t'
        else:
            return f'{self.name} превышает скорость!\t'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


mercedes = SportCar(120, 'blak', 'Mersedes', False)
lada = TownCar(70, 'red', 'Lada', False )
man = WokerCar(39, 'orange', 'Man', False)
volvo = TownCar(60,'grey', 'Volvo', False)
ford = PoliceCar(80, 'white', 'Ford', True)
print(man.turn('left'))
print(f'Когда {lada.turn("right")},то {volvo.stop()}')
print(lada.show_speed())
print(volvo.show_speed())
print(f'Во время {ford.go()}{ford.show_speed()}')
print(mercedes.show_speed())
print(f'{ford.name}, {ford.color}, {ford.is_police},{ford.show_speed()}')














