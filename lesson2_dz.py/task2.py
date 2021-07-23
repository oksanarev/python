# 2 задание.
a = input("Введите символы в свободном порядке: ")
b = list(a)
n = 0
for i in range(int(len(b) / 2)):
    b[n], b[n + 1] = b[n + 1], b[n]
    n += 2

print(b)