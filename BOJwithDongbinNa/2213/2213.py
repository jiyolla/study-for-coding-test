import sys


def solve():
    sys.setrecursionlimit(10**6)
    read = sys.stdin.readline
    n = int(read())
    w = [None] + list(map(int, read().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    # dp[node][is_node_selected] = best answer for sub tree rooted at node with node selected or not
    dp = [[[0, []], [w[i], [i]]] for i in range(n + 1)]

    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                dfs(child)
                if dp[child][1][0] > dp[child][0][0]:
                    dp[node][0][0] += dp[child][1][0]
                    dp[node][0][1] += dp[child][1][1]
                else:
                    dp[node][0][0] += dp[child][0][0]
                    dp[node][0][1] += dp[child][0][1]
                dp[node][1][0] += dp[child][0][0]
                dp[node][1][1] += dp[child][0][1]

    dfs(1)
    if dp[1][1][0] > dp[1][0][0]:
        dp[1][1][1].sort()
        print(f'{dp[1][1][0]}\n{" ".join([str(i) for i in dp[1][1][1]])}')
    else:
        dp[1][0][1].sort()
        print(f'{dp[1][0][0]}\n{" ".join([str(i) for i in dp[1][0][1]])}')


solve()
