import sys


def solve():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    parent = [i for i in range(n + 1)]
    res = []

    def root(v):
        while v != parent[v]:
            v = parent[v]
        return v
    for _ in range(m):
        c, a, b = read().split()
        a, b = int(a), int(b)
        if c == '0':
            # union
            root_a = root(a)
            root_b = root(b)
            if root_a > root_b:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
        else:
            # find
            parent[a] = root(a)
            parent[b] = root(b)
            res.append('YES' if parent[a] == parent[b] else 'NO')
    print('\n'.join(res))


solve()
