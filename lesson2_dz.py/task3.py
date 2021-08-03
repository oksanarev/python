# 3 задание (решение 1)
a = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
m = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if (int(a.index(m)))<=2:
    print("зима")
elif 8<(int(a.index(m)))<=11:
    print("Осень")
if 2<(int(a.index(m)))<=5:
    print("Весна")
elif 5<((int(a.index(m))))<=8:
    print("Лето")

