import sys
import math
import heapq


def solve():
    read = sys.stdin.readline
    v, e = map(int, read().split())
    graph = [{} for _ in range(v + 1)]
    # dist = [[math.inf] * (v + 1) for _ in range(v + 1)]
    # for v1 in range(1, v + 1):
    #     dist[v1][v1] = 0
    for _ in range(e):
        a, b, c = map(int, read().split())
        graph[a][b] = c
        # dist[a][b] = c
    # 루트가 가장 작은 원점으로 돌아오는 사이클을 찾는다라...
    # 플로이드워셜을 한번 돌리고, dist[s][v] + dist[v][s]를 가장 작게 만들어주는 v를 찾으면 되는 거 아녀?
    # 시간 복잡도는 모르겠고 일단 구현.
    # 아니야 생각하고 가보자. 지금 v, e둘다 400아래임. 플로이드워셜 하면 400*400*400걸림 64,000,000흠...가능...?
    # 억까지는 가능하던 거 같은데
    """
    for k in range(1, v + 1):
        for v1 in range(1, v + 1):
            if k == v1:
                continue
            for v2 in range(1, v + 1):
                if k == v2 or v1 == v2:
                    continue
                if dist[v1][v2] > dist[v1][k] + dist[k][v2]:
                    dist[v1][v2] = dist[v1][k] + dist[k][v2]
    min_cycle = math.inf
    for v1 in range(1, v + 1):
        for v2 in range(1, v + 1):
            if v1 != v2 and min_cycle > dist[v1][v2] + dist[v2][v1]:
                min_cycle = dist[v1][v2] + dist[v2][v1]
    print('-1' if math.isinf(min_cycle) else min_cycle)
    """
    # pypy3만 통과.
    # 에지가 적은 것을 잘 활용해야 될 것 같다... 흠
    # 400개의 edge가 이룰 수 있는 구조가 그렇게 복잡한가...?
    # 임의의 노드에서 dijkstra를 해서 다시 임의의 노드가 나오는 첫 순간이 임의의 노드를 시작점으로 하는 최소의 사이클 아닌가?
    # edge가 적으니 빨리 돌 거 같은데. 근데 source노드의 첫 등장이 최소 사이클이 맞는지에 대한 확인이 필요하다.
    # 흠...맞는 거 같은데...
    def dijkstra(start):
        h = []
        dist = [math.inf] * (v + 1)
        dist[start] = 0
        for v2, d2 in graph[start].items():
            dist[v2] = d2
            heapq.heappush(h, (dist[v2], v2))
        while h:
            d1, v1 = heapq.heappop(h)
            if v1 == start:
                return d1
            if dist[v1] < d1:
                continue
            for v2, d2 in graph[v1].items():
                if v2 == start:
                    heapq.heappush(h, (d1 + d2, start))
                    continue
                if dist[v2] > d1 + d2:
                    dist[v2] = d1 + d2
                    heapq.heappush(h, (dist[v2], v2))
        return math.inf
    min_cycle = math.inf
    for s in range(1, v + 1):
        new_cycle = dijkstra(s)
        min_cycle = new_cycle if min_cycle > new_cycle else min_cycle
    print('-1' if math.isinf(min_cycle) else min_cycle)


solve()
