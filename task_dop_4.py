'''Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
'''
s = int(input('Введите общее кол-во журавликов: '))
kat = int(s / 6 * 4)
pet = int(s / 6)
ser = int(s / 6)
print(f'{s} -> {pet} {kat} {ser}')