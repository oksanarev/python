# 7 задание.
from functools import reduce
from itertools import count
def fact (n):
    for i in range(1, n+1):
        yield i

n = int(input('Введите число от 1 до 10: '))

f = 1
i = 1
for el in fact(n):
    f = f * el
    print(f'{el}!= {f}')






