import sys
import math
import heapq


def solve():
    read = sys.stdin.readline
    # sys.setrecursionlimit(10**7)
    for _ in range(int(read())):
        n, m, k = map(int, read().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(k):
            u, v, c, d = map(int, read().split())
            # dp 용
            # graph[v].append((u, c, d))
            # dijkstra용
            graph[u].append((c, d, v))
        for i in range(1, n + 1):
            graph[i].sort()
        # 기본적으로 d에 대해서 다익스트라를 돌리고 싶다.
        # 근데 거기에 c에 대한 제한이 걸린 것이다.
        # 이거 잘하면 dp로 아주 깔끔하게 정리될 것 같은데?
        # 기억하는가? 2차 dp테이블.
        # dp[c][v]를 c라는 코스트 제한 하에 s에서 v까지는 최적값으로 보는 것이다.
        # 그러면 점화식이 어떻게 되냐면, v로 가는 노드의 집합이 U라고 보면
        # dp[c][v] = min(dp[c - u_i][u_i] + cost(u_i, v)), u_i in U 이다.
        # 이러면 다익스트라보다는 밸만포드에 가깝다고 볼 수 있네... 가까운게 아니라 그냥 밸만포득 같은데
        # 오케이 구현해보자.
        # 좀 구체화해야할 것 같다.
        # 어떤식으로 순회해서 dp테이블을 구축할 것인가?
        # dp간만에 하니까 가물가물하네...c를 그냥 0에서 시작해서 m까지 늘리는 게 말이되나? 너무 느린거 아니야..?
        # 하나의 c값에 대해서... 아니 좀 이상한데..
        # 아니 맞는 거 같다. 모든 dp[c][v]는 자기보다 작은 c에 의존하기에, c를 오름차순으로 테이블을 만드는 게 맞다.
        # 그리고 그래프를 읽을 때 거꾸로 저장하는 게 편하다. graph[v]를 v로 시작하는 것이 아닌 v로 끝나는 에지로 저장하는 게 맞다.
        """
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]
        for c in range(0, m + 1):
            dp[c][1] = 0
            for v2 in range(2, n + 1):
                dp[c][v2] = dp[c - 1][v2]
                for v1, c1, d1 in graph[v2]:
                    if c - c1 >= 0 and dp[c][v2] > dp[c - c1][v1] + d1:
                        dp[c][v2] = dp[c - c1][v1] + d1
        print('Poor KCM' if math.isinf(dp[m][n]) else dp[m][n])
        """
        # 아 시간초과가 떠버리네...최악의 경우 100*100*10000*t의 시간이 걸려서...흠
        # pypy3에서도 겨우 통과...
        # 어떻게 최적화를 좀 해볼 수 있을까..
        # 탑다운으로 가볼까...?
        """
        mem = {}

        def topdown_dp(c, v2):
            if (c, v2) in mem:
                return mem[(c, v2)]
            if v2 == 1:
                mem[(c, v2)] = 0
                return 0
            res = math.inf
            for v1, c1, d1 in graph[v2]:
                if c - c1 >= 0:
                    candidate = topdown_dp(c - c1, v1) + d1
                    res = candidate if candidate < res else res
            mem[(c, v2)] = res
            return res
        print('Poor KCM' if math.isinf(topdown_dp(m, n)) else topdown_dp(m, n))
        # pypy3에서도 메모리 초과가 떠버리네...
        """
        # 1등 답 보니까, dp로 dijkstra를 할 수 있는 듯...?
        # dijkstra는 기본적으로 최단 거리의 간선들을 지속적으로 택하는 것인데, 제약이 초과될 때
        # 흠. 제약을 초과하는 순간에 체크해봤자 의미 없다. 그전부터 계속 트래킹해야 된다.
        # 응. 다익스트라에서는 기본적으로 같은 지점을 늦게 방문할 경우는 무시되었는데, 오히려, 일찍 도착한 간선들이 cost를 초과해서
        # cost때문에 방문 못하고, 늦게 도착한 간선이 cost는 높지 않아서 방문할 수도 있겠네, 그러면 기본적으로 일찍 오는 놈들을 선호하기는 하지만
        # cost가 적절한 애만 거르겠네! 대박!.
        h = []
        dist = [[math.inf] * (m + 1) for _ in range(n + 1)]
        heapq.heappush(h, (0, 0, 1))
        dist[1] = [0] * (m + 1)
        while h:
            d, c, v1 = heapq.heappop(h)
            if dist[v1][c] < d:
                continue
            if v1 == n:
                dist[n][m] = d
                break
            for c2, d2, v2 in graph[v1]:
                nc = c + c2
                nd = d + d2
                if nc > m:
                    break
                if dist[v2][nc] > nd:
                    for i in range(nc, m + 1):
                        if nd >= dist[v2][i]:
                            break
                        dist[v2][i] = nd
                    heapq.heappush(h, (nd, nc, v2))
        print('Poor KCM' if math.isinf(dist[n][m]) else dist[n][m])


solve()
