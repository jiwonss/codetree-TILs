num = input().split('.')
n, m = int(num[0]), num[1]

integer_result = bin(n)[2:]
decimal_result = ''
for _ in range(4):
    temp = str(int(m) * 2).zfill(len(m))
    if len(temp) == len(m):
        m = temp
        decimal_result += '0'
    else:
        m = temp[1:]
        decimal_result += '1'
result = integer_result + '.' + decimal_result
print(result)