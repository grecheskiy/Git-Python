def sum_numbers(n, sum=0, a=1):
    sum += a
    if n == 0:
        return sum
    n -= 1
    a = a * (-0.5)
    print(sum)
    return sum_numbers(n, sum, a)


try:
    x = int(input('Enter number: '))
    sum_numbers(x)
except ValueError:
    print('not int, exit')
