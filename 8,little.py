import numpy as np
from typing import List, Tuple, Set

def reduce_matrix(matrix: List[List[float]], reduction_cost: float) -> Tuple[List[List[float]], float]:
    """Выполняет редукцию матрицы по строкам и столбцам."""
    row_mins = [min(row) for row in matrix]
    reduction_cost += sum(row_mins)
    matrix = [[val - row_min for val in row] for row, row_min in zip(matrix, row_mins)]
    
    col_mins = [min(col) for col in zip(*matrix)]
    reduction_cost += sum(col_mins)
    matrix = [[val - col_min for val, col_min in zip(row, col_mins)] for row in matrix]
    
    return matrix, reduction_cost

def find_max_penalty_zero(matrix: List[List[float]]) -> Tuple[int, int, float]:
    """Находит нулевую клетку с максимальной оценкой."""
    max_penalty = -1
    best_i, best_j = -1, -1
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                continue
                
            # Находим минимальные значения в строке и столбце (исключая текущий ноль)
            row_min = min(val for k, val in enumerate(matrix[i]) if k != j and val != np.inf)
            col_min = min(row[j] for k, row in enumerate(matrix) if k != i and row[j] != np.inf)
            
            penalty = row_min + col_min
            if penalty > max_penalty:
                max_penalty = penalty
                best_i, best_j = i, j
                
    return best_i, best_j, max_penalty

def update_paths_and_matrix(matrix: List[List[float]], i: int, j: int, 
                          paths: List[List[int]], visited: Set[int]) -> Tuple[List[List[float]], List[List[int]], Set[int]]:
    """Обновляет пути и матрицу после выбора ребра."""
    # Находим пути, содержащие i и j
    path_i = next((p for p in paths if i in p), None)
    path_j = next((p for p in paths if j in p), None)
    
    # Обновляем пути в зависимости от ситуации
    if path_i and path_j:
        if path_i == path_j:
            # Если оба узла в одном пути - запрещаем цикл
            matrix[path_i[-1]][path_i[0]] = np.inf
        else:
            # Объединяем два пути
            if path_i[0] == i and path_j[-1] == j:
                new_path = path_j + path_i
            elif path_i[-1] == i and path_j[0] == j:
                new_path = path_i + path_j
            else:
                new_path = path_i + path_j[::-1] if path_i[-1] == i and path_j[-1] == j else path_i[::-1] + path_j
                
            paths.remove(path_i)
            paths.remove(path_j)
            paths.append(new_path)
            matrix[new_path[-1]][new_path[0]] = np.inf
    elif path_i:
        # Добавляем j к существующему пути
        if path_i[0] == i:
            path_i.insert(0, j)
        else:
            path_i.append(j)
        visited.add(j)
        matrix[path_i[-1]][path_i[0]] = np.inf
    elif path_j:
        # Добавляем i к существующему пути
        if path_j[-1] == j:
            path_j.append(i)
        else:
            path_j.insert(0, i)
        visited.add(i)
        matrix[path_j[-1]][path_j[0]] = np.inf
    else:
        # Создаем новый путь
        paths.append([i, j])
        visited.update({i, j})
        matrix[j][i] = np.inf
    
    # Запрещаем переходы в выбранные строку и столбец
    for k in range(len(matrix)):
        matrix[i][k] = np.inf
        matrix[k][j] = np.inf
    
    return matrix, paths, visited

def read_graph(filename: str) -> List[List[float]]:
    """Чтение графа из файла."""
    with open(filename) as f:
        return [[float('inf') if val == 'i' else float(val) for val in line.split()] for line in f]

def solve_tsp(matrix: List[List[float]]) -> Tuple[List[int], float]:
    """Решает задачу коммивояжера методом ветвей и границ."""
    matrix = [row[:] for row in matrix]
    total_cost = 0
    paths = []
    visited = set()
    
    for _ in range(len(matrix) - 1):
        matrix, total_cost = reduce_matrix(matrix, total_cost)
        i, j, _ = find_max_penalty_zero(matrix)
        matrix, paths, visited = update_paths_and_matrix(matrix, i, j, paths, visited)
    
    if len(paths) == 1:
        path = paths[0]
    else:
        path = paths[0] + paths[1][::-1]
    
    return path, total_cost

if __name__ == "__main__":
    try:
        graph = read_graph("input.txt")
        path, distance = solve_tsp(graph)
        
        print("Кратчайший гамильтонов цикл:")
        print(" -> ".join(map(str, [x+1 for x in path])))
        print(f"Длина: {distance}")
    except FileNotFoundError:
        print("Ошибка: файл input.txt не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
