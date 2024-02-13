from itertools import permutations

def calc(p):
    result = 0
    for i in range(n):
        temp = 0
        if i - 1 >= 0:
            temp = p[i] - (i - 1)
        if temp > 0:
            result += temp
    return result

n = int(input())
arr = list(map(int, input().split()))

result = 0
for p in permutations(arr, n):
    result = max(result, calc(p))
print(result)