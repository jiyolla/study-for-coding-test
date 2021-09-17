def solve():
    n, k = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]
    mem = {}

    def dp(i, w):
        if i == 0:
            return 0
        elif (i, w) in mem:
            return mem[(i, w)]
        elif items[i - 1][0] > w:
            mem[(i, w)] = dp(i - 1, w)
            return mem[(i, w)]
        else:
            mem[(i, w)] = max(dp(i - 1, w), dp(i - 1, w - items[i - 1][0]) + items[i - 1][1])
            return mem[(i, w)]
    print(dp(n, k))


solve()
