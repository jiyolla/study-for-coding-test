def solve():
    n = int(input())
    ans = [[0] * 10 for _ in range(n)]
    ans[0][1:] = [1] * 9
    for i in range(1, n):
        ans[i][0] = ans[i - 1][1]
        for j in range(1, 9):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j + 1]
        ans[i][9] = ans[i - 1][8]
    print(sum(ans[-1]) % 1000000000)


solve()
