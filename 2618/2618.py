import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    w = int(read())
    work = [tuple(map(int, read().split())) for _ in range(w)]

    def dist(p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])

    # dp[i][j] = minimal distance travelled
    # for first car ending up in ith work and second car ending up in jth work
    # But in fact, we do not need a 2-dimensial array, as a car is always going be on the last work
    # so a trick here
    # dp[i][j] = minimal distance travelled
    # where i = 0 stand for first car ending up in last work and i = 1 vice versa
    # j stand for the last work the other car is end up.
    # Note that, j = 0 means initial position rather than the first work.
    """
    dp = [[None] for _ in range(2)]
    dp[0][0] = dist(work[0], (1, 1))
    dp[1][0] = dist(work[0], (n, n))

    # Tackle ith work(i: direct index at work)
    for i in range(1, w):
        new_dp = [[math.inf] * (i + 1) for _ in range(2)]

        # first car engage
        for j in range(i):
            new_dp[0][j] = dp[0][j] + dist(work[i], work[i - 1])
        new_dp[0][i] = dp[1][0] + dist(work[i], (1, 1))
        for k in range(1, i):
            d = dp[1][k] + dist(work[i], work[k - 1])
            if d < new_dp[0][i]:
                new_dp[0][i] = d

        # second car engage
        for j in range(i):
            new_dp[1][j] = dp[1][j] + dist(work[i], work[i - 1])
        new_dp[1][i] = dp[0][0] + dist(work[i], (n, n))
        for k in range(1, i):
            d = dp[0][k] + dist(work[i], work[k - 1])
            if d < new_dp[1][i]:
                new_dp[1][i] = d
        dp = new_dp
    print(min(min(dp[0]), min(dp[1])))
    """

    # Now deal with traceback
    # Fuck, undoing the trick on state definition seems to be the easiet solution
    # Define dp as straight forward 2d array
    # dp[i][j] = min dist for first car at ith work, second car at jth work,
    # i == j == 0 means initial at position rather at work.
    dp = [[math.inf] * (w + 1) for _ in range(w + 1)]
    dp[1][0] = dist(work[0], (1, 1))
    dp[0][1] = dist(work[0], (n, n))

    # Tackle ith work(i: direct index at work)
    for i in range(1, w):
        # first car engage
        for j in range(i):
            dp[i + 1][j] = dp[i][j] + dist(work[i], work[i - 1])
        dp[i + 1][i] = dp[0][i] + dist(work[i], (1, 1))
        for k in range(1, i):
            d = dp[k][i] + dist(work[i], work[k - 1])
            if dp[i + 1][i] > d:
                dp[i + 1][i] = d

        # second car engage
        for j in range(i):
            dp[j][i + 1] = dp[j][i] + dist(work[i], work[i - 1])
        dp[i][i + 1] = dp[i][0] + dist(work[i], (n, n))
        for k in range(1, i):
            d = dp[i][k] + dist(work[i], work[k - 1])
            if dp[i][i + 1] > d:
                dp[i][i + 1] = d

    a, b, ans = 0, 0, math.inf
    for i in range(w + 1):
        if ans > dp[i][w]:
            a, b, ans = i, w, dp[i][w]
        if ans > dp[w][i]:
            a, b, ans = w, i, dp[w][i]
    print(ans)

    def traceback(last_car, last_work, pre_last_work):
        pre_last_car = next_last_car = 3 - last_car
        next_last_work = 0
        if last_work == 0:
            return [str(pre_last_car)] * pre_last_work
        if last_car == 2:
            ans = dp[0][last_work] + dist(work[last_work], (1, 1))
            for i in range(1, last_work):
                d = dp[i][last_work] + dist(work[last_work], work[i - 1])
                if ans > d:
                    next_last_work, ans = i, d
        else:
            ans = dp[last_work][0] + dist(work[last_work], (n, n))
            for i in range(1, last_work):
                d = dp[last_work][i] + dist(work[last_work], work[i - 1])
                if ans > d:
                    next_last_work, ans = i, d
        print_buf = [str(pre_last_car)] * (pre_last_work - last_work)
        return print_buf + traceback(next_last_car, next_last_work, last_work)

    print('\n'.join(traceback(2 if a > b else 1, b if a > b else a, w)[::-1]))


solve()
