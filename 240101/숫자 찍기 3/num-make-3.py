n, t = map(int, input().split())

# 파스칼의 삼각형 만들기
pascal = [[0 for _ in range(n + 1)] for _ in range(n)]
pascal[0][0] = 1
for i in range(1, n):
    for j in range(n):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

result = [[0 for _ in range(n)] for _ in range(n)]
if t == 1:
    for i in range(n):
        for j in range(n):
            result[i][j] = pascal[i][j]
if t == 2:
    for i in range(n):
        for j in range(n):
            result[i][j] = pascal[n - i - 1][j]
if t == 3:
    for i in range(n):
        for j in range(n):
            result[i][j] = pascal[n - j - 1][n - i - 1]

# 출력
for i in range(n):
    if t == 2:
        print(" " * i, end='')
    for j in range(n):
        if result[i][j] == 0:
            print(" ", end=' ')
        else:
            print(result[i][j], end=' ')
    print()