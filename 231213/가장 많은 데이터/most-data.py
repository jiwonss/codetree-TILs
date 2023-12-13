from collections import defaultdict

n = int(input())
counter = defaultdict(int)
for _ in range(n):
    temp = input()
    counter[temp] += 1
print(sorted(counter.values())[-1])