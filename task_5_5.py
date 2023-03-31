
def tab(i):
    if i > 126:
        return print('%4d-%s' % (i, chr(i)), end=' ')
    if i % 10 == 0:
        print()
    print('%4d-%s' % (i, chr(i)), end=' ')
    return tab(i + 1)


tab(32)