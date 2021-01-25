import sys


def solve():
    read = sys.stdin.readline
    n, _ = int(read()), read()
    parent = [i for i in range(n)]

    def root(v):
        while v != parent[v]:
            v = parent[v]
        return v
    for v1 in range(n):
        for v1_diff, connected in enumerate(read().split()[v1 + 1:]):
            v2 = v1 + v1_diff + 1
            if connected == '1':
                root_v1 = root(v1)
                root_v2 = root(v2)
                if root_v1 > root_v2:
                    parent[root_v1] = root_v2
                else:
                    parent[root_v2] = root_v1
                parent[v1] = parent[root_v1]
                parent[v2] = parent[root_v2]
    query = list(map(int, read().split()))
    ans = root(query[0] - 1)
    for i in query[1:]:
        if root(i - 1) != ans:
            ans = 'NO'
            break
    print(ans if ans == 'NO' else 'YES')


solve()
