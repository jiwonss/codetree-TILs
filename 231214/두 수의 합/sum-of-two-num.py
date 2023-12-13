from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

check = defaultdict(int)
result = 0
for a in arr:
    if check[a]:
        result += 1
    check[a] = k - a
    check[k - a] = a
print(result)