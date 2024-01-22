x, a, y = input().split()
x, y = int(x), int(y)

result = 0
if a == '+':
    result = x + y
if a == '-':
    result = x - y
if a == '*':
    result = x * y
if a == '/':
    result = x // y
print(f'{x} {a} {y} = {result}')