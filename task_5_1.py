def calcul():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operator == '0':
        return print(f'Выход')
    try:
        a = float(input('Введите первое число:'))
    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
        return calcul()
    try:
        b = float(input('Введите второе число:'))
    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
        return calcul()
    if operator == '*':
        print(f'Ваш результат {a * b}')
        return calcul()
    elif operator == '+':
        print(f'Ваш результат {a + b}')
        return calcul()
    elif operator == '-':
        print(f'Ваш результат {a - b}')
        return calcul()
    elif operator == '/':
        if b == 0:
            print(f'На 0 делить нельзя!')
            return calcul()
        else:
            print(f'Ваш результат {a / b}')
            return calcul()
    else:
        print('Не найден такой символ операции, повторите снова')
        return calcul()


calcul()
