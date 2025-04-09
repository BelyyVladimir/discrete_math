inf = float('inf')
matrix = [[inf,2,inf,4,14],
          [2,inf,6,8,inf],
          [3,inf,inf,5,6],
          [inf,6,5,inf,9],
          [7,8,7,2,inf]]
start = 1
finish = 4

n = len(matrix)
d = [inf] * n
local_d = [inf] * n
d[start-1] = 0
v = start - 1

not_used = [True]*n
not_used[start - 1] = False

local_d = [inf] * n

while (v != finish - 1):
    for u in range (n):
        if not_used[u]: local_d[u] = min(local_d[u],d[v] + matrix[v][u])
    v = local_d.index(min(local_d))
    d[v] = min(local_d)
    local_d[v] = inf

print(d[finish-1])

