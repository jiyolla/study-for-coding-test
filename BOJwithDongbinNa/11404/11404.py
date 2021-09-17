import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    dist = [[math.inf] * (n + 1) for _ in range(n + 1)]
    for v in range(1, n + 1):
        dist[v][v] = 0
    for _ in range(m):
        v1, v2, d = map(int, read().split())
        if dist[v1][v2] > d:
            dist[v1][v2] = d

    # Floyd Warshall
    for v in range(1, n + 1):
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                if dist[v1][v2] > dist[v1][v] + dist[v][v2]:
                    dist[v1][v2] = dist[v1][v] + dist[v][v2]
    res = []
    for i in range(1, n + 1):
        res.append(' '.join(['0' if math.isinf(j) else str(j) for j in dist[i][1:]]))
    print('\n'.join([str(i) for i in res]))


solve()
