n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    if i - 1 < 0:
        temp = arr[i] + (i - 1)
    else:
        temp = arr[i] - (i - 1)
    if temp > 0:
        result += temp
print(result)