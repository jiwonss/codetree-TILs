n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    result.append(arr[i] + [sum(arr[i])])
temp = []
for r in zip(*result):
    temp.append(sum(r))
result.append(temp)

for i in range(n + 1):
    for j in range(n + 1):
        print(result[i][j], end=' ')
    print()