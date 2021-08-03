# 5задание.
s = [6, 4, 2, 1]
i = 1
b = int(input("Введите число (очки): "))
while i != 0:
    s.append(b)
    b =sorted(s)
    s = list(reversed(b))
    print("Рейтинг на данный момент: ", s)
    i = int(input("Вы хотите продолжить? Да - 1, нет - 0: ")) * i
    b = int(input("Введите число (очки): ")) if i == 1 else  print("Окончательный рейтинг", s)




