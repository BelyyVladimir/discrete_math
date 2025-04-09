from collections import deque
def wave_algorithm(matrix):
    start = end = None
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == -2:
                start = (i, j)
            elif val == -3:
                end = (i, j)

    if not start or not end:
        return None
    queue = deque([start])
    matrix[start[0]][start[1]] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return matrix[x][y] - 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                if matrix[nx][ny] == 0 or matrix[nx][ny] == -3:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))

    return None

n = int(input("Введите размер матрицы: "))
print("Введите матрицу:")
print(" -1 - стена (непроходимая клетка)")
print(" -2 - старт")
print(" -3 - финиш")
print("  0 - свободная клетка")

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
distance = wave_algorithm(matrix)

if distance is not None:
    print(f"Кратчайший путь: {distance}")
else:
    print("Путь не найден")
