def s_calc(arg1, arg2):
    res = arg1 / arg2
    return res
try:
    arg1 = float(input('Введите первое число: '))
    arg2 = float(input('Введите второе число: '))
except ValueError:
    print('!')
else:
    print(s_calc(arg1, arg2))