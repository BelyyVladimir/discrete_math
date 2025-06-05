import numpy as np
from typing import List, Tuple

def bfs(residual_graph: List[List[int]], source: int, sink: int, parent: List[int]) -> bool:
    visited = [False] * len(residual_graph)
    queue = [source]
    visited[ource] = True
    
    while queue:
        u = queue.pop(0)
        
        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                
                if v == sink:
                    return True
                    
    return False

def ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    residual_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u
        
        max_flow += path_flow
        
    return max_flow

def read_graph_from_file(filename: str) -> Tuple[List[List[int]], int, int]:
    """Чтение графа из файла."""
    with open(filename) as f:
        graph = [[int(num) for num in line.split()] for line in f]
    return graph, 0, len(graph) - 1 

if __name__ == "__main__":
    input_file = "input.txt"
    graph, source, sink = read_graph_from_file(input_file)
    max_flow = ford_fulkerson(graph, source, sink)
    print(f"Максимальный поток равен {max_flow}")
