import sys


def solve():
    read = sys.stdin.readline
    v, e = map(int, read().split())
    edges = sorted([tuple(map(int, read().split())) for _ in range(e)], key=lambda x:x[2])
    parent = [i for i in range(v + 1)]
    size = [1 for _ in range(v + 1)]

    def find(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(v1, v2):
        root_v1 = find(v1)
        root_v2 = find(v2)
        if root_v1 == root_v2:
            return False
        else:
            parent[root_v1] = root_v2
            size[root_v2] += size[root_v1]
            return True

    ans = 0
    for a, b, c in edges:
        if union(a, b):
            ans += c
            if size[b] == v:
                break
    print(ans)


solve()
