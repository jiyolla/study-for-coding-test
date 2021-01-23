import sys
import heapq
import math


def solve():
    read = sys.stdin.readline
    for _ in range(int(read())):
        n, m, t = map(int, read().split())
        s, g, h = map(int, read().split())
        graph = [{} for _ in range(n + 1)]
        for _ in range(m):
            a, b, d = map(int, read().split())
            graph[a][b] = d * 2
            graph[b][a] = d * 2
        dests = [int(read()) for _ in range(t)]
        # 이게 시발 운발이 좋아서 문제 없는 거 아닌가?
        # 한번 곰곰히 생각해보자.
        # 그니까 원래 값으로 보면, g-h가 0.5작아지면 선택되고, 그대로면 선택 안 되는 상황이 있는가?
        # 0.5만 작아져서 변화가 생겼다면 적어도 원래 채택되었던 간선과의 차이가 0.5이하였다는 거구 그러면 실질적으로는
        # 같았다는 뜻이다...즉, 애초에 둘 다 채택될 수 있는 상황이었으니 문제가 최적해에 영향을 안 끼친다 ㄷㄷ....
        # 시발 문제 없네...오케이 인정..
        graph[g][h] -= 1
        graph[h][g] -= 1

        def dijkstra(start, *end):
            h = []
            heapq.heappush(h, (0, start))
            dist = [math.inf for _ in range(n + 1)]
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
        """
        d_s_g, d_s_h, *d_s_dests = dijkstra(s, *([g, h] + dests))
        d_g_dests = dijkstra(g, *dests)
        d_h_dests = dijkstra(h, *dests)
        res = []
        for i in range(t):
            # 시발. d_s_dests[i]가 inf일 때 처리 안 한 거 찾는 데 ㅈㄴ 오래걸렸다...
            if d_s_dests[i] == min(d_s_g + d_h_dests[i], d_s_h + d_g_dests[i]) + graph[g][h] and not math.isinf(d_s_dests[i]):
                res.append(dests[i])
        print(*sorted(res))
        """
        d_s_dests = dijkstra(s, *dests)
        res = []
        for i in range(t):
            if d_s_dests[i] % 2 == 1:
                res.append(dests[i])
        print(*sorted(res))


solve()
