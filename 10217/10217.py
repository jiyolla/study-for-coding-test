import sys
import math


def solve():
    read = sys.stdin.readline
    for _ in range(int(read())):
        n, m, k = map(int, read().split())
        graph = [{} for _ in range(n + 1)]
        for _ in range(k):
            u, v, c, d = map(int, read().split())
            graph[u][v] = (c, d)
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
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]
        for _ in range(n - 1):
            for v1 in range(1, n + 1):
                for v2, c, d in graph.items():
                    if dp[][]


solve()
