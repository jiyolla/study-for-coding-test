import sys


def solve():
    sys.setrecursionlimit(10**6)
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    # dp[for_tree_rooted_at][w/_or_wo/_root_being_early_adopter] = min_num_early_adopters
    dp = [[0, 1] for _ in range(n + 1)]

    # Bottom Up approach would be difficult,
    # because we have to travarse the tree in descending depth manner which
    # requires a depth labeling preprocess before the traversal.
    # Though not that hard, anyway, we'll do top down way.
    visited = [False] * (n + 1)

    def min_ea(node):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                min_ea(child)
                dp[node][0] += dp[child][1]
                dp[node][1] += dp[child][0] if dp[child][0] < dp[child][1] else dp[child][1]

    min_ea(1)
    print(min(dp[1]))
    # Amazingly Simple!


solve()
