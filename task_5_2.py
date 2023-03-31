def count_number(n, even=0, odd=0):
    if n <= 0:
        return print(f'in number {n}, even {even}, odd {odd}')
    else:
        n_end = n % 10
        n = n // 10
        if n_end % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_number(n, even, odd)


try:
    x = int(input('Enter number: '))
    count_number(x)
except ValueError:
    print('not int, exit')
