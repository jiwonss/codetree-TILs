def multi(n):
    for i in range(1, 10):
        print(f'{n} * {i} = {n * i}')

num = sorted(list(map(int, input().split())))

for i in range(num[0], num[2] + 1):
    if i == num[1]:
        continue
    multi(i)