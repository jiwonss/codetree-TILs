N, M = input().split()

M = int(M)
alpha = {chr(i + 65) : i + 10 for i in range(26)}

result = 0
for i, n in enumerate(N[::-1]):
    result += (M ** i) * int(n if n.isdigit() else alpha[n])
print(result)