def power(k):
    if k == 1:
        return 3
    return 3 * power(k - 1)

n = int(input())
print(power(n))