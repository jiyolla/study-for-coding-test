import sys
import heapq
import math


def solve():
    read = sys.stdin.readline
    v, e = map(int, read().split())
    graph = [{} for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, d = map(int, read().split())
        if v2 in graph[v1]:
            graph[v1][v2] = min(graph[v1][v2], d)
            graph[v2][v1] = min(graph[v2][v1], d)
        else:
            graph[v1][v2] = d
            graph[v2][v1] = d
    v_1, v_2 = map(int, read().split())

    def dijkstra(start, *end):
        h = []
        heapq.heappush(h, (0, start))
        dist = [math.inf for _ in range(v + 1)]
        dist[start] = 0
        while h:
            d1, v1 = heapq.heappop(h)
            if dist[v1] < d1:
                continue
            for v2, d2 in graph[v1].items():
                if dist[v2] > d1 + d2:
                    dist[v2] = d1 + d2
                    heapq.heappush(h, (dist[v2], v2))
        return tuple([dist[i] for i in end])

    # 여기서 엄청난 발견이 있다. 1 -> v_1 -> v_2 -> v와 1 -> v_2 -> v_1 -> v중에서 더 작은 것을 골라야 되는데
    # 방향이 없는 그래프이기에, 1 -> v_1과 v_1 -> 1이 같다. 다른 간선들도 모두 마찬가지다.
    # 그래서 dijkstra를 최소한으로 돌리기 위해서는, 시작 노드의 수를 최대한 줄이는 것이 좋다.
    # 그래서 v_1 -> 1, v_1 -> v_2, v_1 -> v를 한방에 구하고
    # 마찬가지로 v_2 -> 1, v_2 -> v를 한방에 구하는 것이다.
    d_v1_1, d_v1_v2, d_v1_v = dijkstra(v_1, 1, v_2, v)
    d_v2_1, d_v2_v = dijkstra(v_2, 1, v)
    res = min(d_v1_1 + d_v2_v, d_v2_1 + d_v1_v) + d_v1_v2
    print(-1 if math.isinf(res) else res)


solve()
