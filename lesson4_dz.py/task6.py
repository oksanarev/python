# 6 Задание.
from itertools import count, cycle

#for el in count(4):
#    print(el)
#    if el == 77:
#        break



b = [x for x in range(20)]
a = [1, 4, 5, 23, 1]
gen = cycle(a)
for i in b:
    print(next(gen))


