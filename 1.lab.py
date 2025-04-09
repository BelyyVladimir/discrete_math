class Connectivity:
    def first_algorithm(graph):
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


    def second_algorithm(graph):
        vertices_count = len(graph)
        parent = list(range(vertices_count))

        def find(parent_array, vertex):
            if parent_array[vertex] != vertex:
                parent_array[vertex] = find(parent_array, parent_array[vertex])
            return parent_array[vertex]

        def union(parent_array, x, y):
            root_x = find(parent_array, x)
            root_y = find(parent_array, y)
            if root_x != root_y:
                parent_array[root_y] = root_x

        for i in range(vertices_count):
            for j in range(vertices_count):
                if graph[i][j] != 0:
                    union(parent, i, j)

        roots = set()
        for i in range(vertices_count):
            roots.add(find(parent, i))
        return len(roots)

graph1 = [
        [0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 1, 0]
    ]
graph2 = [
        [0, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 0]
    ]
print(f"Число компонент связности 1 алг 1 граф = {Connectivity.first_algorithm(graph1)}")
print(f"Число компонент связности 2 алг 1 граф = {Connectivity.second_algorithm(graph1)}")

print(f"Число компонент связности 1 алг 2 граф = {Connectivity.first_algorithm(graph2)}")
print(f"Число компонент связности 2 алг 2 граф = {Connectivity.second_algorithm(graph2)}")
