# 4 задание.
# Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую
#построчно данные. При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

tr = {'One':'Один', 'Two':'Два','Three':'Три', 'Four':'Четыре'}
new_line = []
with open('text4.txt',encoding='UTF-8') as my_f:
    for i in my_f:
        i = i.split()
        print(i)
        s = [''.join(tr.get(i[0])), i[1], i[2],'\n']
        str_s = " ".join(s)
        print(str_s)
        new_line.append(str_s)
        with open('text4.1.txt', 'w', encoding='UTF-8') as my_f1:
            for j in new_line:
                my_f1.write(j)




