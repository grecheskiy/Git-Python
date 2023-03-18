a = int(input('Введите шестизначный номер билета: '))
b = int(a / 1000)
c = int(a % 1000)
sum1 = int(b / 100 + (b / 10) % 10 + b % 10)
sum2 = int(c / 100 + (c / 10) % 10 + c % 10)
if sum1 == sum2:
    print(f'{a} -> yes')
else:
    print(f'{a} -> no')