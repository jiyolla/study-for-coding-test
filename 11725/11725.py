import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    parent = [None] * (n + 1)
    parent[1] = 1
    stack = [1]
    while stack:
        cur = stack.pop()
        for child in adj[cur]:
            if parent[child] is None:
                parent[child] = cur
                stack.append(child)

    print_buf = []
    for node in range(2, n + 1):
        print_buf.append(f'{parent[node]}')
    print('\n'.join(print_buf))


solve()
