from sys import argv

script_name, time_work, pay_hours, plus_pay = argv

time_work = int(time_work)
pay_hours = float(pay_hours)
plus_pay = int(plus_pay)
pay = time_work * pay_hours + plus_pay
print("Зарплата за месяц составила - ", pay, "руб.")
