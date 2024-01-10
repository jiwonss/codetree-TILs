def subset(start, arr):
    global result
    if start == n:
        if check(arr):
            result = max(result, len(arr))
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = 1
        arr.append(num[i])
        subset(i + 1, arr)
        arr.pop()
        visited[i] = 0

def check(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            return 0
    return 1

n, a, d = map(int, input().split())
num = list(map(int, input().split()))

visited = [0 for _ in range(n)]
start = num.index(a)
result = 0
subset(start, [])
print(result)