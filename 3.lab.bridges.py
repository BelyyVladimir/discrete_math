def alg_1_lab(graph):
    vertices_count = len(graph)
    vertices = list(range(vertices_count))
    visited_vertices = []
    connectivity_components = []

    if vertices:
        initial = 0
        if initial in vertices:
            vertices.remove(initial)
            visited_vertices.append(initial)

    while vertices:
        i = 0
        while i < len(visited_vertices):
            current = visited_vertices[i]
            for j in range(vertices_count):
                if graph[current][j] != 0 and j not in visited_vertices:
                    visited_vertices.append(j)
                    if j in vertices:
                        vertices.remove(j)
            i += 1

        connectivity_components.append(visited_vertices.copy())
        visited_vertices.clear()

        if vertices:
            next_vertex = vertices[0]
            visited_vertices.append(next_vertex)
            vertices.remove(next_vertex)
    return len(connectivity_components)

matrix = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]]
verts_count = len(matrix)
bridge_edge = []
defoult_con = alg_1_lab(matrix)
for a in range (verts_count):
    for b in range(verts_count):
        graph_test = matrix.copy()
        graph_test[a][b] = 0
        graph_test[b][a] = 0
        if defoult_con != alg_1_lab(graph_test):
            bridge_edge.append([a, b])

print(bridge_edge)



