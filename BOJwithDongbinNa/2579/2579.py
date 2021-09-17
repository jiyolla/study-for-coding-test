import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    ans = [[0] * 3 for _ in range(n)]
    stage = int(read())
    ans[0][1] = stage
    for i in range(1, n):
        stage = int(read())
        ans[i][0] = max(ans[i - 1][1], ans[i - 1][2])
        ans[i][1] = ans[i - 1][0] + stage
        ans[i][2] = ans[i - 1][1] + stage
    print(max(ans[-1][1:]))


solve()
