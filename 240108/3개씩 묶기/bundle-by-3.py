n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(0, n, 3):
    if i + 3 - 1 < n:
        result += sum(arr[i:i + 3][:-1])
    else:
        result += sum(arr[i:])
print(result)