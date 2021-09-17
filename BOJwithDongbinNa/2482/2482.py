from operator import add


def solve():
    n = int(input())
    k = int(input())

    # dp[i][j][k] = count of choice sequence with i(0or1), end by j(0or1) and chosen k colors
    # eg. dp[0][1][3] would mean the first color(what ever it is) isn't selected,
    # that last color(seen) is selected and the sequence has total 3 colors selected.
    # To be more specific, say we have N = 6 and K = 3, and colors are named C1~C6.
    # And we are inspecting on C5.
    # That is, we have known every possible choice for K<=3 for C1~C4.
    # now dp[0][1][3] would mean, C1 is selected, C4 is selected and C2, C3 are also selected
    # We need to know whether the first color is selected or not for the last decision
    # The last color is selected or not for current decision(including the last decision)
    # and Numbers of color selected for not exceeding K.
    # No more information needed to make the best choice.

    dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(2)]
    dp[0][0][0] = 1
    dp[1][1][1] = 1
    for i in range(n - 1):
        new_dp = [[None for _ in range(2)] for _ in range(2)]
        for first in range(2):
            # Select current color
            new_dp[first][1] = [0] + dp[first][0][:-1]

            # Or not
            new_dp[first][0] = list(map(add, dp[first][0], dp[first][1]))
        dp = new_dp
        # print(f'Round: {i}\n'
        #        f'dp[0][0] = {dp[0][0]}\n'
        #        f'dp[0][1] = {dp[0][1]}\n'
        #        f'dp[1][0] = {dp[1][0]}\n'
        #        f'dp[1][1] = {dp[1][1]}')
    print((dp[0][0][-1] + dp[0][1][-1] + dp[1][0][-1]) % 1000000003)


solve()
