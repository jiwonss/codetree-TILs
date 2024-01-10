def solve(a, d):
    if a not in arr:
        return 0
    cnt, num = 1, a + d
    for i in range(arr.index(a), n):
        if arr[i] == num:
            cnt += 1
            num += d 
    return cnt    

n, a, d = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(a, d))