def subset(idx, arr):
    global result
    if idx == n:
        if arr and check(arr):
            result = max(result, len(arr))
        return
    subset(idx + 1, arr)
    subset(idx + 1, arr + [num[idx]])

def check(arr):
    global a
    if arr[0] != a:
        return 0
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            return 0
    return 1

n, a, d = map(int, input().split())
num = list(map(int, input().split()))

visited = [0 for _ in range(n)]
result = 0
subset(0, [])
print(result)