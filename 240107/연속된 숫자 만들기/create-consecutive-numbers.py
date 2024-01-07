def check(a, b, c):
    if c - b == 1 and c - a == 2:
        return 1
    return 0

def move(a, b, c):
    global cnt, min_cnt, max_cnt
    if check(a, b, c):
        min_cnt = min(min_cnt, cnt)
        max_cnt = max(max_cnt, cnt)
        cnt = 0
        return 
    if a + 1 < b:
        a, b, c = a, a + 1, b
        cnt += 1
        move(a, b, c)
    if a + 2 < b:
        a, b, c = a, a + 2, b
        cnt += 1
        move(a, b, c)
    if b + 1 < c:
        a, b, c = b, b + 1, c
        cnt += 1
        move(a, b, c)
    if b + 2 < c:
        a, b, c = b, b + 2, c
        cnt += 1
        move(a, b, c)

p1, p2, p3 = map(int, input().split())

cnt = 0
min_cnt, max_cnt = 1e9, 0
move(p1, p2, p3)
print(min_cnt)
print(max_cnt)