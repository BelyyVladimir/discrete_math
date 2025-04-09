def kruskal(adj_matrix):
    num_vertices = len(adj_matrix)
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = adj_matrix[i][j]
            if weight > 0:
                edges.append((weight, i, j))
    edges.sort()
    total_weight = 0
    edges_added = 0
    for weight, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            total_weight += weight
            edges_added += 1
            if edges_added == num_vertices - 1:
                break

    return total_weight

def prima(mat):
    total_weight = 0
    vis = [1]
    while len(vis) != len(mat):
        min_edge = 0
        ind = 0
        for i in vis:
            k = i - 1
            for j in range(len(mat)):
                if (mat[k][j] < min_edge or min_edge == 0) and ((j + 1) not in vis) and (mat[k][j] != 0):
                    min_edge = mat[k][j]
                    ind = j + 1
        vis.append(ind)
        total_weight += min_edge

    return total_weight

matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]]

result1 = kruskal(matrix)
result2 = prima(matrix)

print(f"Вес минимального остовного дерева: {result1}")
print(f"Вес минимального остовного дерева: {result2}")
