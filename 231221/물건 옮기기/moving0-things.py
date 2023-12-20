n = int(input())

status = {}
result = 0
for _ in range(n):
    num, loc = map(int, input().split())
    if status.get(num):
        if status[num] == loc:
            continue
        result += 1
    else:
        status[num] = loc
print(result)