A, B = map(int, input().split())

start, end = A, A
idx, result = 0, 0
while True:
    if idx % 2 == 0:
        start = end
        end = A + 2 ** idx
    else:
        start = end
        end = A - 2 ** idx
    if start > end and end <= B <= start:
        result += (B - end)
        break 
    if start <= end and start <= B <= end:
        result += (B - start)
        break
    result += abs(start - end)
    idx += 1
print(result)