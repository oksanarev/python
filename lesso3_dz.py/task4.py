# 4 задание.
def my_fanc (x, y):
     m = 1 / (x**abs(y))
     return print(f"Результатом возведения {x} в степень {y} = {m:0.02}")
my_fanc(int(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))
