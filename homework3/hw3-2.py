import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return ProMatrix(self.matrix + other.matrix)

    def __mul__(self, other):
        return ProMatrix(self.matrix * other.matrix)

    def __matmul__(self, other):
        return ProMatrix(self.matrix @ other.matrix)

    def __str__(self):
        return str(self.matrix)


class PropertyMixin:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value


class FileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())


class WriteMixin:
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


class ProMatrix(PropertyMixin, FileMixin, WriteMixin, Matrix):
    pass


np.random.seed(0)
a = np.random.randint(0, 10, (5, 10))
b = np.random.randint(0, 10, (10, 10))

ma = ProMatrix(a)
mb = ProMatrix(b)

z1 = ma + mb
z2 = ma * mb
z3 = ma @ mb

z1.save_to_file('artifacts/hw3-2/matrix_add.txt')
z2.save_to_file('artifacts/hw3-2/matrix_mul.txt')
z3.save_to_file('artifacts/hw3-2/matrix_matmul.txt')
