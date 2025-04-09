inf = float('inf')
m = [[0,2,inf,4,14],
    [2,0,6,8,inf],
    [3,inf,0,5,6],
    [inf,6,5,0,9],
    [7,8,7,2,0]]
start = 1
d = [inf]*5
d[start - 1] = 0

flag = 0
for i in range (5):
    flag = 0
    for a in range (5):
        for b in range (5):
            if m[a][b] != inf  and d[b] != inf and d[a] > d[b] + m[a][b]:
                d[a] = d[b] + m[a][b]
                flag = 1
if flag:
    print("есть контур отрицательного веса")
else:
    print(m)
