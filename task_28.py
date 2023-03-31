def sum_numbers(a, b):
    if b == 0:
        return print(f'sum numbers: {a}')
    else:
        try:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
        except ValueError:
            print("!")
        if a >= -1 and b > -1 or a > -1 and b >= -1:
            a += 1
            b -= 1
            return sum_numbers(a, b)
        else:
            print('not correct numbers')
