'''
list_1 = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
mes = int(input('Введите месяц в виде целого числа от 1 до 12: '))
for item in list_1.keys():
    if mes in list_1[item]:
        print(item)

'''
list_1 = ['Зима', 'Весна', 'Лето', 'Осень']
mes = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if mes == 12 or mes == 1 or mes == 2:
    print(list_1[0])
elif mes == 3 or mes == 4 or mes == 5:
    print(list_1[1])
elif mes == 6 or mes == 7 or mes == 8:
    print(list_1[2])
elif mes == 9 or mes == 10 or mes == 11:
    print(list_1[3])
else:
    print('Error')

