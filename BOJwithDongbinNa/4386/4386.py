import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    points = [tuple(map(float, read().split())) for _ in range(n)]
    parent = [i for i in range(n + 1)]
    size = [1 for _ in range(n + 1)]
    edges = []

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

    def dist(p1, p2):
        return pow((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2, 0.5)

    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i != j:
                edges.append((dist(p1, p2), i, j))
    edges.sort()
    ans = 0
    for d, v1, v2 in edges:
        if union(v1, v2):
            ans += d
            if size[v2] == n:
                break
    print(ans)


solve()
