inf = float('inf')
m = [[0,2,inf,4,14],
    [2,0,6,8,inf],
    [3,inf,0,5,6],
    [inf,6,5,0,9],
    [7,8,7,2,0]]

for a in range (5):
    for b in range (5):
        for c in range (5):
            if m[b][a] != inf and m[a][c] != inf:
                if m[b][c] > m[b][a] + m[a][c]:
                    m[b][c] = m[b][a] + m[a][c]
flag = 1
for a in range(5):
    if m[a][a] != 0: flag = 0
if flag:
    print(m)
else:
    print("есть контур отрицательного веса")


