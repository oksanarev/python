# 3 задание.
def my_func (a, b, c):
    s = [a, b, c]
    min_1 = min(s)
    s.remove(min_1)
    sum_s = sum(s)
    return print(f"Сумма наибольших аргументов = {sum_s}")

my_func(int(input("Введите 1-ое число: ")), int(input("Введите 2-ое число: ")), int(input("Введите 3-е число: ")))