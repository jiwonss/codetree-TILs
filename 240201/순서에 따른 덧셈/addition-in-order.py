from itertools import permutations

def calc():
    result = 0
    for i in range(n):
        if i - 1 < 0:
            temp = arr[i] + (i - 1)
        else:
            temp = arr[i] - (i - 1)
        if temp > 0:
            result += temp
    return result

n = int(input())
arr = list(map(int, input().split()))

result = 1e9
for p in permutations(arr, n):
    result = min(result, calc())
print(result)