#5 задание.

from functools import reduce

def mult_a(a, b):
    return a*b
a = [el for el in range(100, 1001) if el % 2 ==0]
print(f'Список чётных чисел от 100 до 1000, a = {a}')
d = reduce(mult_a, a)
print(f'Результат вычисления произведения всех элементов ({d})')
#pr_my_list = reduce(lambda x, y: x*y, my_list)
#print(f'результат вычисления произведения = {pr_my_list}')

