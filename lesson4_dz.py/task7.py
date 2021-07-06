# 7 задание.
<<<<<<< HEAD
from functools import reduce
from itertools import count
=======

>>>>>>> b50c218 (exchange_task7)
def fact (n):
    for i in range(1, n+1):
        yield i

n = int(input('Введите число от 1 до 10: '))

f = 1
i = 1
for el in fact(n):
    f = f * el
    print(f'{el}!= {f}')

<<<<<<< HEAD





=======
>>>>>>> b50c218 (exchange_task7)
