﻿# 1 задание.
# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_obj = open('text1.txt', 'w+')

while True:
    s = input('Введите строку: ')
    if s == " " or len(s) ==0: break
    file_obj.write(s + '\n')

file_obj.close()
