# 1 задание.
a = input("Как Вас зовут? ")
b = int(input("Какое сегодня число?" ))
elements = ["Мой список",2021 ,True]
elements.insert(2 , a)
elements.insert(4 , b)
print(elements)
for el in elements:
    print(type(el))