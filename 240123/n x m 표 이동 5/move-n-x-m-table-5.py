from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]
    
    q.append([0, 0])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])
    return 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs())