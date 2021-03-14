import sys
import math


def solve():
    sys.setrecursionlimit(10**5)
    read = sys.stdin.readline
    n = int(read())
    populations = [None] + list(map(int, read().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    # Consider a sub-tree rooted at v with the entire tree rooted at r:
    # There could be at most 4 factors should be taken care of.
    # 1. v's parent; 2. v; 3. v's children; 4. v's grandchildren
    # To be specific,
    # v can only be bestowed if
    # 1. None of v's childrens are bestowed
    # v can onl
    # Clear.
    # dp[node][state]
    # state = 00, 01, 1
    # 00: me unselected, all children unseleccted
    # 01: me unselected, at least on children selected
    # 1: me selected
    # dp[node][1] = max(dp[child][00~01]) for each child + self
    # dp[node][01] = max(dp[child][01~1]) for each child and at least one dp[child][1]
    # dp[node][00] = dp[child][01]
    # This should work.
    # max(dp[root][01~1]) gives the answer
    # code 00->0, 01->1, 1->2

    dp = [[0, 0, populations[i]] for i in range(n + 1)]
    visited = [False] * (n + 1)

    def max_elected(node):
        visited[node] = True
        min_diff = math.inf
        for child in adj[node]:
            if not visited[child]:
                max_elected(child)
                dp[node][0] += dp[child][1]
                if min_diff > dp[child][1] - dp[child][2]:
                    min_diff = dp[child][1] - dp[child][2]
                dp[node][1] += dp[child][1] if dp[child][1] > dp[child][2] else dp[child][2]
                dp[node][2] += dp[child][0] if dp[child][0] > dp[child][1] else dp[child][1]
        if min_diff > 0:
            # This makes sense even when the node is a leaf node
            # which means it will directly enter here
            # and sets dp[node][1] as -math.inf
            # It is amazingly correct as it avoids its parent node choosing this branch
            # as it is a leaf node and it has no children thus state=01 does not hold
            dp[node][1] -= min_diff

    max_elected(1)
    print(max(dp[1][1:]))


solve()
