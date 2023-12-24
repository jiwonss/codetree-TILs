n = int(input())
arr = list(map(int, input().split()))
for a in sorted(arr, reverse=True):
    print(a, end=" ")