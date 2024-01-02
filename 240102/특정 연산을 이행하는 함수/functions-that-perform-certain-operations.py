num = list(map(int, input().split()))

for n in num:
    if n % 2 == 0:
        print(n // 2, end=' ')
    else:
        print(n * 3 - 20, end=' ')