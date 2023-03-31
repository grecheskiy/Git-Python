def revers_number(n, r=0):
    if n % 10 == 0:
        return print(f'Revers number: {r}')
    else:
        temp = n % 10
        n = n // 10
        r = r * 10
        r = r + temp
        return revers_number(n, r)


try:
    x = int(input('Enter number: '))
    revers_number(x)
except ValueError:
    print('not int, exit')
