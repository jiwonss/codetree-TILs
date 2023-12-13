n, m = map(int, input().split())
dic1, dic2 = {}, {}
for i in range(1, n + 1):
    temp = input()
    dic1[i] = temp
    dic2[temp] = i
for _ in range(m):
    temp = input()
    if temp.isdigit():
        print(dic1[int(temp)])
    else:
        print(dic2[temp])