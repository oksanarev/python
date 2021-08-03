# 4 задание.
a = input("Введите строку из нескольких слов, разделив их пробелами: ")
c = a.split( )
for ind, el in enumerate(c, 1):
     print(f"{ind}, {el[:10]}")
