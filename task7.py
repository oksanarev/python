#7 задание.
#. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).

from json import dumps

res = [{}, {}]

with open('text7.txt', encoding='UTF-8') as my_file:
    l = my_file.readlines()
    for i in l:
        name, firm, plus, minus = i.split()
        s = name
        p = int(plus)
        m = int(minus)
        res[0][s] = p - m
        res[1]['average_profit'] = sum(profit for _, profit in res[0].items() if profit > 0) / len(res[0])

print(f'{res}')
with open('text7.json', 'w') as j_file:
    j_file.write(dumps(res))
    j = dumps(res)
print(j)