n = int(input())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
board = [[0 for _ in range(n)] for _ in range(n)]

mid = n // 2
board[mid][mid] = 'A'

cnt, num = 1, 1
for i in range(mid, 0, -1):
    for j in range(mid - cnt, (mid - cnt) + 2 * cnt + 1):
        board[j][i - 1] = alphabet[num % 26]
        num += 1
    cnt += 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            print(" ", end=' ')
        else:
            print(board[i][j], end=' ')
    print()