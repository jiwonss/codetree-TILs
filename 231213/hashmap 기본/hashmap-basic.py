n = int(input())
hashmap = {}
for _ in range(n):
    op = input().split()
    if op[0] == 'add':
        k, v = int(op[1]), int(op[2])
        hashmap[k] = v
    if op[0] == 'remove':
        k = int(op[1])
        del hashmap[k]
    if op[0] == 'find':
        k = int(op[1])
        print(hashmap.get(k))