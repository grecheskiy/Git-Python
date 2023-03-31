from random import randint


def rand_number(num, i=1):
    print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
    if i > 10:
        return print('Вы исчерпали 10 попыток. Было загадано', num)
    else:
        try:
            n = int(input(f'{i}-я попытка: '))
        except ValueError:
            print('Вы ввели строку, а нужно вводить цифры')
            return rand_number(num, i)
        if n > num:
            print('меньше')
            i += 1
        elif n < num:
            print('больше')
            i += 1
        else:
            return print('Вы угадали')
        return rand_number(num, i)


x = randint(0, 100)
rand_number(x)
