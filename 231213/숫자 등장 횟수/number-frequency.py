from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))
target = list(map(int, input().split()))

counter = Counter(arr)
for t in target:
    print(counter[t], end=' ')