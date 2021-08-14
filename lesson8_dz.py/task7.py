# 7 Задание.
#Реализовать проект «Операции с комплексными числами». Создайте
# класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 + z2  = ')
        return f'{self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        print(f'Произведеие z1 * z2 =')
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}*i'

    def __str__(self):
        return f'{self.z} = {self.a} + {self.b}*i'

z1 = ComplexNumber(2, 7)
z2 = ComplexNumber(4, -2)
print(z1)
print(z1+z2)
print(z1 * z2)

