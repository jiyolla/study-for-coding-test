import sys
import heapq
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    adj = [[] for _ in range(n + 1)]
    adj_inv = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, cost = map(int, read().split())
        adj[start].append((end, cost))
        adj_inv[end].append((start, cost))
    start, end = map(int, read().split())
    h = [(0, start)]
    cost = [math.inf] * (n + 1)
    cost[start] = 0
    while h:
        cost_src, src = heapq.heappop(h)
        if src == end:
            break
        if cost[src] < cost_src:
            continue
        for dst, cost_dst in adj[src]:
            if cost[dst] > cost_src + cost_dst:
                heapq.heappush(h, (cost_src + cost_dst, dst))
                cost[dst] = cost_src + cost_dst
    route = [str(end)]
    cur = end
    while cur != start:
        for src, cost_from_src in adj_inv[cur]:
            if cost_from_src + cost[src] == cost[cur]:
                cur = src
                route.append(str(cur))
                break
    print(f'{cost[end]}\n{len(route)}\n{" ".join(route[::-1])}')


solve()
