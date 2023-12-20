n = int(input())

status = [[-1] for _ in range(11)]
for _ in range(n):
    num, loc = map(int, input().split())
    if status[num][-1] != loc:
        status[num].append(loc)

result = 0
for s in status:
    if len(s[1:]) > 0:
        result += len(s[1:]) - 1
print(result)