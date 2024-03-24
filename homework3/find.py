import numpy as np


class HashMixin:
    def __hash__(self):
        # Преобразуем матрицу в плоский список элементов
        flat_matrix = sum(self.matrix, [])
        # Вычисляем хеш как комбинацию размеров матрицы и суммы её элементов
        return hash((self.row, self.column)) ^ hash(sum(flat_matrix))


class Matrix(HashMixin):
    def __init__(self, matrix):
        self.row = len(matrix)
        self.column = len(matrix[0])
        if isinstance(matrix, np.ndarray):
            self.matrix = matrix.tolist()
        elif isinstance(matrix, list):
            self.matrix = matrix
        else:
            raise TypeError("The input must be a numpy ndarray or a list")


def find_collisions(n, max_value=100):
    # Инициализируем словарь для хранения хешей и соответствующих им матриц
    hashes = {}
    collisions = []

    for _ in range(n):
        # Генерируем случайный размер матрицы
        rows, cols = np.random.randint(1, 5, size=2)
        # Генерируем матрицу с случайными значениями
        matrix = np.random.randint(0, max_value, size=(rows, cols))
        m = Matrix(matrix)
        h = hash(m)

        if h in hashes:
            # Если хеш уже существует, проверяем не является ли это коллизией
            for prev_matrix in hashes[h]:
                if m.matrix != prev_matrix.matrix:
                    collisions.append((m.matrix, prev_matrix.matrix))
        else:
            hashes[h] = []

        hashes[h].append(m)

    return collisions


# Попробуем найти коллизии, проверив 10000 различных матриц
collisions = find_collisions(1000)

# Выведем количество найденных коллизий и первые несколько примеров
len(collisions),
print(collisions[:1])
