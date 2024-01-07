def check(a, b, c):
    if c - b == 1 and c - a == 2:
        return 1
    return 0

def move(a, b):
    div, mod = divmod(a + b, 2)
    if mod == 0:
        return div
    return div + 1

p1, p2, p3 = map(int, input().split())

# 최소
a, b, c = p1, p2, p3
min_cnt = 0
while not check(a, b, c):
    result1, result2 = move(a, b), move(b, c)
    if (result1 - a) > (result2 - b):
        a, b = b, result2
    else:
        c, b = b, result1
    min_cnt += 1
print(min_cnt)

# 최대
a, b, c = p1, p2, p3
max_cnt = 0
while not check(a, b, c):
    result1, result2 = move(a, b), move(b, c)
    if (result1 - a) < (result2 - b):
        a, b = b, result2
    else:
        c, b = b, result1
    max_cnt += 1
print(max_cnt)