def move(idx):
    a, b = idx
    if info[a][1] + info[b][1] <= info[b][0]:
        info[b][1] += info[a][1]
        info[a][1] = 0
    else:
        info[a][1] = info[a][1] + info[b][1] - info[b][0]
        info[b][1] = info[b][0]


info = [list(map(int, input().split())) for _ in range(3)]

idx = [[0, 1], [1, 2], [2, 0]]
for i in range(100): 
    move(idx[i % 3])

for i in range(3):
    print(info[i][1])