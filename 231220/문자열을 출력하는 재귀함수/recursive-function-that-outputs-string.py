def solve(k):
    if k == 1:
        print("Coding is my favorite hobby!")
        return
    print("Coding is my favorite hobby!")
    solve(k - 1)

n = int(input())
solve(n)