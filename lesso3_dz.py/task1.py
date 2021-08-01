# 1 задание.

def div_num (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError :
        return "Число b не может быть 0"
    except ValueError :
        return "Введите число!"

print("Результат a/b: ",div_num (int(input("Введите число a: ")),(int(input("Введите число b: ")))))