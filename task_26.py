def numbers(a, b, result=1):
    if b == 0:
        return print(f'result: {result}')
    else:
        result = result * a
        b = b - 1
    return numbers(a, b, result)


try:
    x = int(input('Enter number: '))
    y = int(input('Enter inc: '))
    numbers(x, y)
except ValueError:
    print('not int, exit')
