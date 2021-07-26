# 6 задание.
def int_func(*args):

    return args
word = input('Введите любое слово на анг. яз.: ')
sent = input('Введите предложение на англ. яз.: ')
print(int_func((word.title()), (sent.title())))

