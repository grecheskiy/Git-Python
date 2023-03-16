'''
Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
'''
n = int(input('Введите размер стороны n: '))
m = int(input('Введите размер стороны m: '))
k = int(input('Введите кол-во долек: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print(f'{n} {m} {k} -> yes')
else:
    print(f'{n} {m} {k} -> no')