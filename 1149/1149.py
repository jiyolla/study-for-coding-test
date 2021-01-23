import sys


def solve():
    read = sys.stdin.readline
    n = int(read())

    line = list(map(int, read().split()))
    ans = [line] + [[0, 0, 0] for _ in range(n - 1)]
    for i in range(1, n):
        line = list(map(int, read().split()))
        ans[i][0] = min(ans[i - 1][1], ans[i - 1][2]) + line[0]
        ans[i][1] = min(ans[i - 1][0], ans[i - 1][2]) + line[1]
        ans[i][2] = min(ans[i - 1][0], ans[i - 1][1]) + line[2]
    print(min(ans[-1]))


solve()
