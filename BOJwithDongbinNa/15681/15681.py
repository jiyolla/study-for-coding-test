import sys


def solve():
    sys.setrecursionlimit(10**6)
    read = sys.stdin.readline
    n, r, q = map(int, read().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    size = [1] * (n + 1)

    def dfs(node):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                size[node] += dfs(child)
        return size[node]

    dfs(r)

    print_buf = []
    for _ in range(q):
        print_buf.append(f'{size[int(read())]}')
    print('\n'.join(print_buf))


solve()
