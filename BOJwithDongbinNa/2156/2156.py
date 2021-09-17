import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    ans = [[0] * 3 for _ in range(n)]
    ans[0][1] = int(read())
    for i in range(1, n):
        vol = int(read())
        ans[i][0] = max(ans[i - 1])
        ans[i][1] = ans[i - 1][0] + vol
        ans[i][2] = ans[i - 1][1] + vol
    print(max(ans[-1]))


solve()
