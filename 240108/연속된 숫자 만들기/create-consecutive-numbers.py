a, b, c = map(int, input().split())

# 최소 이동 횟수
min_cnt = 2
if b - a == 2 or c - b == 2:
    min_cnt = 1
elif b - a == 1 and c - b == 1:
    min_cnt = 0
print(min_cnt)

# 최대 이동 횟수
max_left, max_right = b - a - 1, c - b - 1
print(max_left if max_left > max_right else max_right)