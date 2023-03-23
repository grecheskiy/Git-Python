'''
def my_func(arg1, arg2, arg3):
    if arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
print(my_func(a, b, c))
'''
def my_func(*args):
    list_1 = [arg1, arg2, arg3]
    list_1.sort()
    res = list_1[1] + list_1[2]
    return res
arg1 = int(input('Enter number 1: '))
arg2 = int(input('Enter number 2: '))
arg3 = int(input('Enter number 3: '))
print(my_func(arg1, arg2, arg3))

