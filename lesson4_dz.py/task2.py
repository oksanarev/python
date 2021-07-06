# 2 задание.

my_list = [23, 45, 6, 1, 3, 34, 123, 24]

new_list = [el for num, el in enumerate (my_list)if my_list[num] > my_list[num - 1]]

print(f'my_list = {my_list}')
print(f'new_list = {new_list}')

