# 5 задание.
a = input("Введите числа через пробел: ").split()
res_1 = [int(el)for el in a]
sum_res = sum(res_1)
print(f"Сумма Ваших чисел =  {sum_res}")
pr = False
while pr == False:
    a = input('Введите ещё числа или Q для выхода - ').split()
    res = 0
    for el in range(len(a)):
        if a[el] == 'q' or a[el] == 'Q':
            pr = True
            break

        else:
            res = res + int(a[el])
    sum_res = sum_res + res
    print(f'Сумма всех ваших чисел = {sum_res}')
print(f'Финальная сумма = {sum_res}')
