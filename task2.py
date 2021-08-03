# 2 задание.
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

#my_f = open('text2.txt')
#content = my_f.read()
#print(f'Содержимое файла: {content}')
#my_f = open('text2.txt')
#content1 = my_f.readlines()
#print(f'Количество строк содержиого: {len(content1)}')
#my_f = open('text2.txt')
#content = my_f.read()
#content = content.split()
#print(f'Количество слов: {len(content)}')

#my_f.close()
with open('text2.txt', 'r') as my_f:
    line = 0
    for i in my_f:
        line += 1
    print(f'Строк в тексте файла:{line}')
with open("text2.txt") as my_f:
    content = my_f.read()
    print(content)
    content = content.split()
    print(f'В тексте файла {len(content)} слов.')



