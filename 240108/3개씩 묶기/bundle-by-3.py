n = int(input())
arr = sorted(list(map(int, input().split())))

result = 0
for i in range(0, n, 3):
    result += sum(arr[i:i + 3][1:])
print(result)