import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        summat = ''
        for i in range(len(self.matrix)):
            summat = summat + '\t'.join(map(str, self.matrix[i])) + '\n'
        return summat

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
a = Matrix(m1)
b = Matrix(m2)
print(a)
print(b)
c = a + b
print('result: ')
print(c)
print(type(c))
