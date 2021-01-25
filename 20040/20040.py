import sys


def solve():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    parent = [i for i in range(n)]

    def find(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(v1, v2):
        root_v1 = find(v1)
        root_v2 = find(v2)
        if root_v1 != root_v2:
            parent[root_v1] = root_v2
            return True
        else:
            return False

    cycle_found = False
    for i in range(m):
        v1, v2 = map(int, read().split())
        if not union(v1, v2):
            cycle_found = True
            break
    if cycle_found:
        print(i + 1)
    else:
        print(0)


solve()
