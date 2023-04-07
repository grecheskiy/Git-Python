def songs(stroka):
    stroka = stroka.split()
    list_1 = []
    for word in stroka:
        summa = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                summa += 1
        list_1.append(summa)
    return len(list_1) == list_1.count(list_1[0])


text = input("Введите фразу: ")
if songs(text):
    print('Парам пам-пам')
else:
    print('Пам парам')