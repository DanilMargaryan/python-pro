import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.row = len(matrix)
        self.column = len(matrix[0])
        if isinstance(matrix, np.ndarray):
            self.matrix = matrix.tolist()
        elif isinstance(matrix, list):
            self.matrix = matrix
        else:
            raise TypeError("The input must be a numpy ndarray or a list")

    def _check_dimensions(self, other):
        if self.row != other.row or self.column != other.column:
            raise ValueError("Matrices must have the same dimensions.")

    def __add__(self, other):
        self._check_dimensions(other)
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.column)] for i in
                       range(self.row)])

    def __mul__(self, other):
        self._check_dimensions(other)
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(self.column)] for i in
                       range(self.row)])

    def __matmul__(self, other):
        if self.column != other.row:
            raise ValueError(
                "Matrix A's number of columns must equal Matrix B's number of rows for multiplication")
        result = [[0 for _ in range(other.column)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(other.column):
                for k in range(self.column):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)


def save_variable_to_file(variable_value, file_name):
    with open(file_name, 'w') as file:
        file.write(variable_value)


np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

ma = Matrix(a)
mb = Matrix(b)

z1 = ma + mb
z2 = ma * mb
z3 = ma @ mb

save_variable_to_file(str(z1.matrix), 'artifacts/hw3-1/matrix_add.txt')
save_variable_to_file(str(z2.matrix), 'artifacts/hw3-1/matrix_mul.txt')
save_variable_to_file(str(z3.matrix), 'artifacts/hw3-1/matrix_matmul.txt')
