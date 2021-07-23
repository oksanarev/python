# 3 задание (вариант 2)
a = {'winter':(12, 1, 2),'spring':(3, 4, 5),'summer':(6, 7, 8),'autumn':(9, 10, 11)}
m = int(input('Введите месяц в виде целого числа от 1 до 12: '))
w = list(a.get('winter'))
s = list(a.get('spring'))
su = list(a.get('summer'))
au = list(a.get('autumn'))
if m in w:
         print('Это зимний месяц.')
elif m in s:
        print('Это весенний месяц.')
elif m in su:
        print('Это летний месяц.')
elif m in au :
        print('Это осень.')

