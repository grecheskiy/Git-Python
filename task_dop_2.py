'''
Найдите сумму цифр трехзначного числа.
'''
a = int(input('Введите трехзначное число: '))
n = int(a / 100)
nn = int((a / 10) % 10)
nnn = int(a % 10)
print(f'sum numbers {n + nn + nnn}')