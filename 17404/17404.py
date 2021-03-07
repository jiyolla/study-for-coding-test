import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    cost = [list(map(int, read().split())) for _ in range(n)]

    # dp[i][j] = best cost ever coloring first house as i and last house as j
    dp = [[0] * 3 for _ in range(3)]
    dp[0] = [cost[0][0], math.inf, math.inf]
    dp[1] = [math.inf, cost[0][1], math.inf]
    dp[2] = [math.inf, math.inf, cost[0][2]]
    for i in range(1, n):
        new_dp = [[0] * 3 for _ in range(3)]
        for color_0 in range(3):
            new_dp[color_0][0] = min(dp[color_0][1], dp[color_0][2]) + cost[i][0]
            new_dp[color_0][1] = min(dp[color_0][0], dp[color_0][2]) + cost[i][1]
            new_dp[color_0][2] = min(dp[color_0][0], dp[color_0][1]) + cost[i][2]
        dp = new_dp
    for i in range(3):
        dp[i][i] = math.inf
    print(min([item for row in dp for item in row]))


solve()
