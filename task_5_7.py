def get_sum(n):
    if n == 0:
        return n
    else:
        print(f'{n} + ', end='')
        return n + get_sum(n - 1)


n = int(input('n = '))
print(get_sum(n))
print(f'{n}({n}+1)/2 = {n * (n + 1) / 2}')
