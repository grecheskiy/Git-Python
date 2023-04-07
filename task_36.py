def print_operation_table(operation, num_rows, num_сolums):
    array = [[operation(i, j) for i in range(1, num_rows+1)] for j in range(1, num_сolums+1)]
    for i in array:
        print(*[f"{x:>3}"for x in i])


line = int(input("Введите количество строк: "))
colums = int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x * y, line, colums)