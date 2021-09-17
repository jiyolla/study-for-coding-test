import sys
sys.setrecursionlimit(10**7)


def solve():
    m, n = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(m)]
    routes = {(0, 0): 1}

    def dp(row, col):
        print(routes)
        print(f'[enter] r: {row}, c:{col}')
        if (row, col) in routes:
            return routes[(row, col)]
        ans = 0
        if row + 1 < m and mt[row + 1][col] > mt[row][col]:
            ans += dp(row + 1, col)
        if row > 0 and mt[row - 1][col] > mt[row][col]:
            ans += dp(row - 1, col)
        if col + 1 < n and mt[row][col + 1] > mt[row][col]:
            ans += dp(row, col + 1)
        if col > 0 and mt[row][col - 1] > mt[row][col]:
            ans += dp(row, col - 1)
        routes[(row, col)] = ans
        print(f'[exit]  r: {row}, c:{col}')
        return ans

    print(dp(m - 1, n - 1))


solve()
