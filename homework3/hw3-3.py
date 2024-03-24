import numpy as np


class HashMixin:
    def __hash__(self):
        # Преобразуем матрицу в плоский список элементов для упрощения вычислений
        flat_matrix = sum(self.matrix, [])
        # Вычисляем хеш как комбинацию размеров матрицы и суммы её элементов
        # Для этого используем XOR (^) между хешами этих значений
        return hash((self.row, self.column)) ^ hash(sum(flat_matrix))


class Matrix(HashMixin):
    _multiplication_cache = {}  # Словарь для кэширования результатов умножения

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
        self._check_dimensions(other)

        # Создаём ключ для кэша на основе хешей текущей и второй матрицы
        cache_key = (hash(self), hash(other))
        # Проверяем, есть ли уже результат в кэше
        # if cache_key in Matrix._multiplication_cache:
        #     return Matrix._multiplication_cache[cache_key]

        result = [[0 for _ in range(other.column)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(other.column):
                for k in range(self.column):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        # Сохраняем результат в кэш перед возвратом
        Matrix._multiplication_cache[cache_key] = Matrix(result)
        return Matrix(result)


def save_variable_to_file(variable_value, file_name):
    with open(file_name, 'w') as file:
        file.write(variable_value)


A = Matrix([[61, 33, 90], [41, 59, 0], [20, 43, 27]])
C = Matrix([[84, 56, 98], [45, 4, 29], [22, 4, 32]])
B = Matrix([[8, 9, 3], [8, 8, 0], [5, 3, 9]])
D = Matrix([[8, 9, 3], [8, 8, 0], [5, 3, 9]])

AB = A @ B
CD = C @ D

print(A.__hash__())
print(C.__hash__())
hash_ABCD = f'AB = {AB.__hash__()}\nCD = {CD.__hash__()}'

# [[1202, 1083, 993], [800, 841, 123], [639, 605, 303]]
# [[1610, 1498, 1134], [537, 524, 396], [368, 326, 354]]

save_variable_to_file(str(A.matrix), 'artifacts/hw3-3/A.txt')
save_variable_to_file(str(B.matrix), 'artifacts/hw3-3/B.txt')
save_variable_to_file(str(C.matrix), 'artifacts/hw3-3/C.txt')
save_variable_to_file(str(D.matrix), 'artifacts/hw3-3/D.txt')

save_variable_to_file(str(AB.matrix), 'artifacts/hw3-3/AB.txt')
save_variable_to_file(str(CD.matrix), 'artifacts/hw3-3/CD.txt')

save_variable_to_file(str(hash_ABCD), 'artifacts/hw3-3/hash_ABCD.txt')
