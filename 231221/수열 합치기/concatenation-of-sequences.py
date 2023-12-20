n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = sorted(A + B)
for a in arr:
    print(a, end=' ')