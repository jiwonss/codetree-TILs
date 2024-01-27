def calc(num):
    num.replace('\r', '')
    carry, result = 0, ''
    for n in num[::-1]:
        temp = int(n) * 2
        if carry:
            temp += carry
            carry = 0
        if temp >= 10:
            carry = temp // 10
            result += str(temp % 10)
        else:
            result += str(temp)
    if carry:
        result += str(carry)
    return result[::-1]

num = input().split('.')
n, m = int(num[0]), num[1]

integer_result = bin(n)[2:]
decimal_result = ''
for _ in range(4):
    temp = calc(m)
    if len(m) == len(temp):
        decimal_result += '0'
        m = temp
    else:
        m = temp[1:]
        decimal_result += '1'

result = integer_result + '.' + decimal_result
print(result)