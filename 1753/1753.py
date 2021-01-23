import sys
import heapq
import math


def solve():
    read = sys.stdin.readline

    v, e = map(int, read().split())
    s = int(read())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, w = map(int, read().split())
        graph[v1].append((v2, w))
    dist = [math.inf for _ in range(v + 1)]
    hq = []
    dist[s] = 0
    heapq.heappush(hq, (0, s))
    while hq:
        cost, v1 = heapq.heappop(hq)
        for v2, w in graph[v1]:
            if dist[v2] > cost + w:
                dist[v2] = cost + w
                heapq.heappush(hq, (dist[v2], v2))
    res = [str(i).upper() for i in dist[1:]]
    print('\n'.join(res))


solve()
